from source.call_tex import render_pdflatex, render_xelatex
from source.tex_style import get_english_style, get_chinese_style_kaiti
import matplotlib.pyplot as plt
from source.frame import *
from source.render_frame import render_one, blend_with_background
from source.video_maker import get_default_video_maker_args, make_video_ffmpeg


twoColFrameStyle = get_two_column_chn_eng_frame_default_style()
twoColFrame = get_two_column_chn_eng_frame('两列帧','Two Columns', ['和','差','积','商'],
                                           ['Sum', 'Difference', 'Product', 'Quotient'], twoColFrameStyle)
twoColFrame.duration = 8.0
mathFrame = get_math_frame()
mathFrame.duration = 8.0


make_video_ffmpeg('test.mp4', [twoColFrame, mathFrame], get_default_video_maker_args())
