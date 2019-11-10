from source.frame import _get_default_text_entity, _get_default_line_entity, _get_section_marker_dict
from source.frame import *

chn_sec = None
eng_sec = None

def quick_section_marker(chn_title, eng_title):
    global chn_sec, eng_sec
    chn_sec = chn_title
    eng_sec = eng_title

def quick_section_title_frame():
    frame = Frame()
    frame['chn_title'] = _get_default_text_entity(
        text=chn_sec,
        style='chn',
        x=h_center,
        y=frame_size[1] - 400,
        size=25
    )

    frame['eng_title'] = _get_default_text_entity(
        text=eng_sec,
        style='eng',
        x=h_center,
        y=RelativeY('chn_title', -60),
        size=16
    )

    return frame

def condition_add_section_marker(frame):
    if chn_sec is not None and eng_sec is not None:
        titleDict = _get_section_marker_dict()
        titleDict['sec_chn_title']['text'] = chn_sec
        titleDict['sec_eng_title']['text'] = eng_sec
        frame.entities.update(titleDict)

def quick_math_frame(chn_title, eng_title, eqn, chn_caption, eng_caption):
    frame = get_math_frame()
    frame['chn_title']['text'] = chn_title
    frame['eng_title']['text'] = eng_title
    frame['equation']['text'] = eqn
    frame['chn_caption']['text'] = chn_caption
    frame['eng_caption']['text'] = eng_caption
    condition_add_section_marker(frame)
    return frame

def quick_two_column_chn_eng_frame(chn_title, eng_title, col1, col2):
    frame = get_two_column_chn_eng_frame(chn_title, eng_title, col1, col2, get_multicol_frame_default_style())
    condition_add_section_marker(frame)
    return frame

def quick_three_column_eng_chn_eng_frame(chn_title, eng_title, col1, col2, col3):
    style = get_multicol_frame_default_style()
    style['left_right_margin'] = 400
    style['mid_margin'] = 80
    frame = get_three_column_eng_chn_eng_frame(chn_title, eng_title, col1, col2, col3, style)
    condition_add_section_marker(frame)
    return frame

def quick_title_frame(chn_title, eng_title):
    frame = Frame()
    frame['chn_title'] = _get_default_text_entity(
        text=chn_title,
        style='chn',
        x=h_center,
        y=frame_size[1]-400,
        size=30
    )

    frame['eng_title'] = _get_default_text_entity(
        text=eng_title,
        style='eng',
        x=h_center,
        y=RelativeY('chn_title', -80),
        size=20
    )

    return frame
