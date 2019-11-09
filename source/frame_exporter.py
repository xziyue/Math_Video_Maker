from source.render_frame import render_one, blend_with_background
import os


# export all frames to a folder
def export_all_frames(frames, folder, incremental=False, fmt='frame_{:03d}'):
    for ind, frame in enumerate(frames):
        filename = os.path.join(folder, fmt.format(ind + 1) + '.jpg')
        if incremental:
            if os.path.exists(filename):
                continue
        print('exporting frame {}/{}'.format(ind + 1, len(frames)))
        img = blend_with_background(render_one(frame)).convert('RGB')
        img.save(filename)

