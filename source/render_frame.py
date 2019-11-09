from PIL import Image
from skimage.color import rgba2rgb, rgb2gray
from source.call_tex import render_pdflatex, render_xelatex
from source.tex_style import get_chinese_style_kaiti, get_english_style
from multiprocessing.pool import ThreadPool
from source.frame import frame_size, RelativeY
import numpy as np
from source.get_root_dir import get_root_dir
import os
import matplotlib.pyplot as plt

rootDir = get_root_dir()
resDir = os.path.join(rootDir, 'res')
backgroundFilename = os.path.join(resDir, 'background.png')
imgBg = Image.open(backgroundFilename).convert('RGBA')
assert imgBg.size == frame_size

# allow 8 concurrent threads
threadPool = ThreadPool(8)

def _resolve_relative_y(frame, renderedObj, target, mode=None):
    if isinstance(frame[target]['y'], RelativeY):
        relativeY = frame[target]['y']
        resolveResult = _resolve_relative_y(frame, renderedObj, relativeY.objName, relativeY.mode)
        if mode == 'top' or mode == 'bottom':
            frame[target]['y'] = resolveResult + relativeY.offset
        elif mode == 'center':
            refCenter = resolveResult + renderedObj[relativeY.objName].size[1]//2
            frame[target]['y'] = refCenter + renderedObj[target].size[1]//2
        else:
            raise AttributeError('unknown mode: ' + mode)
    else:
        if mode == 'bottom' or mode == 'center':
            return frame[target]['y'] - renderedObj[target].size[1]
        elif mode == 'top':
            return frame[target]['y']
        else:
            raise AttributeError('unknown mode: ' + mode)


# crop text images to the bounding box
def _crop_text_image(img):
    # convert to gray scale
    grayImg = rgb2gray(rgba2rgb(img))
    pxLoc = np.where(grayImg[:, :] < 0.95)
    min1, max1 = pxLoc[0].min() - 1, pxLoc[0].max() + 1
    min2, max2 = pxLoc[1].min() - 1, pxLoc[1].max() + 1
    min1, min2 = max(min1, 0), max(min2, 0)
    max1, max2 = min(max1, img.shape[0] - 1), min(max2, img.shape[1] - 1)
    return img[slice(min1, max1), slice(min2, max2), :]
    #return grayImg

def _generate_text_task(key, func, data):
    img = func(data)
    return (key, _crop_text_image(img))

def render_one(frame, content_alpha=1.0):
    renderedObj = dict()

    taskQueue = []
    for key, val in frame.items():
        if val['type']=='text':
            if len(val['text']) == 0:
                renderedObj[key] = np.zeros((1, 1, 4), np.uint8)
                continue
            if val['style'] == 'eng':
                texData = get_english_style(val['text'], val['size'])
                taskQueue.append((key, render_pdflatex, texData))
            elif val['style'] == 'chn':
                texData = get_chinese_style_kaiti(val['text'], val['size'])
                taskQueue.append((key, render_xelatex, texData))
            else:
                raise AttributeError('unknown style: {}'.format(val['style']))
        elif val['type']=='line':
            img = np.zeros([val['height'], val['width'], 4], np.uint8)
            img[:, :, -1].fill(255)
            renderedObj[key] = Image.fromarray(img)
        else:
            raise AttributeError('unknown type: {}'.format(val['type']))

    # generate the text concurrently
    textResult = threadPool.starmap(_generate_text_task, taskQueue)
    for key, img in textResult:
        assert img is not None
        #plt.imshow(img)
        #plt.show()
        renderedObj[key] = Image.fromarray(img)

    # resolve relative positions
    for key, val in frame.items():
        if isinstance(val['y'], RelativeY):
            _resolve_relative_y(frame, renderedObj, key, val['y'].mode)

    for key, item in frame.items():
        if isinstance(item['y'], RelativeY):
            raise RuntimeError('unable to resolve relative Y position for \"{}\"'.format(item))

    # assemble the frame
    imgFrame = Image.new('RGBA', frame_size, 0)

    for key, val in frame.items():
        x = val['x']
        y = imgFrame.size[1] - val['y']
        # check alignment
        if val['alignment'] == 'c':
            width = renderedObj[key].size[0]
            x -= width // 2
        imgFrame.paste(renderedObj[key], (x, y), renderedObj[key])

    return imgFrame


def blend_with_background(foreground, alpha=1.0):
    foreground = np.asarray(foreground).copy()
    foreground[:, :, -1] = np.round(np.clip(foreground[:, :, -1].astype(np.float) * alpha, 0.0, 255.0)).astype(np.uint8)
    foreground = Image.fromarray(foreground)
    frameImg = imgBg.copy()
    frameImg.paste(foreground, (0, 0), foreground)

    return frameImg