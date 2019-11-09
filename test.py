import matplotlib.pyplot as plt
from source.frame import *
from source.quick_frame import *
from source.video_maker import get_default_video_maker_args, make_video_ffmpeg
from source.frame_exporter import export_all_frames


frames = []

frames.append(quick_math_frame('准备！', 'Prepare!', r'\parbox{4cm}{\begin{gather*}a+b\\b+c\end{gather*}}', 'HAHA!', 'HAHA!'))

frames.append(quick_title_frame('常见数学展示', 'Common Math Presentation'))
frames.append(quick_two_column_chn_eng_frame('两列帧','Two Columns', ['和','差','积','商'],
                                           ['Sum', 'Difference', 'Product', 'Quotient']))
frames.append(get_math_frame())


export_all_frames(frames, 'build')
