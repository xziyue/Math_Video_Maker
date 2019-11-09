import cv2
from source.frame import frame_size
from source.render_frame import render_one, blend_with_background
import numpy as np
import subprocess
from io import BytesIO

def get_default_video_maker_args():
    return {
        'fps' : 20,
        'transition_time' : 0.4,
        'max_bitrate' : '1500k',
        'buf_size' : '1024k'
    }


def make_video_cv2(outname, frames, args):
    out = cv2.VideoWriter(outname, cv2.VideoWriter_fourcc(*'DIVX'), args['fps'], frame_size)
    transitionFrames = round(args['transition_time'] * args['fps'])
    transitionAlpha1 = np.linspace(0.0, 1.0, transitionFrames)
    transitionAlpha2 = np.linspace(1.0, 0.0, transitionFrames)

    frameTime = 1.0 / args['fps']

    for frame in frames:
        if frame.duration < 2.0 * args['transition_time']:
            raise RuntimeError('frame duration too short')

    for ind, frame in enumerate(frames):
        print('writing frame {}/{}'.format(ind + 1, len(frames)))

        # create a render schedule
        numFrames = round(frame.duration / frameTime)
        alphas = np.ones(numFrames, np.float)
        alphas[:transitionAlpha1.size] = transitionAlpha1
        alphas[-transitionAlpha2.size:] = transitionAlpha2

        # render the content
        frameContent = render_one(frame)

        for alpha in alphas:
            img = blend_with_background(frameContent, alpha).convert('RGB')
            newImg = np.asarray(img).copy()
            newImg = cv2.cvtColor(newImg, cv2.COLOR_RGB2BGR)
            out.write(np.asarray(newImg))

    out.release()



# makes x264 video
def make_video_ffmpeg(outname, frames, args):
    transitionFrames = round(args['transition_time'] * args['fps'])
    transitionAlpha1 = np.linspace(0.0, 1.0, transitionFrames)
    transitionAlpha2 = np.linspace(1.0, 0.0, transitionFrames)

    # quantize alphas into discrete values to save computations
    transitionAlpha1 = np.round((transitionAlpha1 * 255.0)).astype(np.int)
    transitionAlpha2 = np.round((transitionAlpha2 * 255.0)).astype(np.int)

    frameTime = 1.0 / args['fps']
    for frame in frames:
        if frame.duration < 2.0 * args['transition_time']:
            raise RuntimeError('frame duration too short')

    fpsStr = repr(args['fps'])
    # open ffmpeg process
    p = subprocess.Popen(
        ['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', fpsStr,
         '-i', '-', '-vcodec', 'libx264', '-maxrate', args['max_bitrate'],
         '-bufsize', args['buf_size'],
         '-r', fpsStr, outname], stdin=subprocess.PIPE
    )

    for ind, frame in enumerate(frames):
        print('writing frame {}/{}'.format(ind + 1, len(frames)))

        # create a render schedule
        numFrames = round(frame.duration / frameTime)
        alphas = np.zeros(numFrames, np.int)
        alphas.fill(255)
        alphas[:transitionAlpha1.size] = transitionAlpha1
        alphas[-transitionAlpha2.size:] = transitionAlpha2

        # render the content
        frameContent = render_one(frame)

        uniqueAlphas = np.unique(alphas)
        alpha2Img = dict()
        for alpha in uniqueAlphas:
            io = BytesIO()
            img = blend_with_background(frameContent, alpha/255.0).convert('RGB')
            img.save(io, 'JPEG', quality=95)
            io.seek(0)
            alpha2Img[alpha] = io.read()

        for alpha in alphas:
            p.stdin.write(alpha2Img[alpha])

    p.stdin.close()
    p.wait()



