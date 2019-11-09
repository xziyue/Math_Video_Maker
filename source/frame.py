def _get_default_entity(**kwargs):
    result = {
        'type' : None,
        'alignment' : 'c',
        'x' : 0,
        'y' : 0,
        'hint' : '',
        'duration' : 0.0
    }

    for key, val in kwargs.items():
        result[key]=val

    return result

def _get_default_text_entity(**kwargs):
    result= _get_default_entity(
        type='text',
        text='',
        style='eng',
        size=30
    )

    for key, val in kwargs.items():
        result[key]=val

    return result

def _get_default_line_entity(**kwargs):
    result=_get_default_entity(
        type='line',
        height=2,
        width =100
    )

    for key, val in kwargs.items():
        result[key] = val

    return result


class RelativeY:
    def __init__(self, objName, offset, mode='bottom'):
        self.objName = objName
        self.offset = offset
        self.mode=mode # bottom/top/center

frame_size = (1920, 1080)
h_center = frame_size[0] // 2


def _get_frame_title_dict():
    result = dict()

    result['chn_title'] = _get_default_text_entity(
        text='帧测试',
        style='chn',
        x=h_center,
        y=frame_size[1] - 40,
        size=13
    )

    result['title_sep'] = _get_default_line_entity(
        width=600,
        height=2,
        x=h_center,
        y=RelativeY('chn_title', -10),
    )

    result['eng_title'] = _get_default_text_entity(
        text='Frame Test',
        style='eng',
        x=h_center,
        y=RelativeY('title_sep', -10),
        size=11
    )

    return result

def _get_section_marker_dict():
    result = dict()

    result['sec_chn_title'] = _get_default_text_entity(
        text='标题',
        style='chn',
        x=150,
        y=frame_size[1] - 8,
        size=6
    )

    result['sec_eng_title'] = _get_default_text_entity(
        text='Title',
        style='eng',
        x=150,
        y=RelativeY('sec_chn_title', -8),
        size=3
    )

    return result


class Frame():

    def __init__(self, duration=1.0):
        self.duration = 1.0
        self.entities = dict()

    def __getitem__(self, item):
        return self.entities[item]

    def __setitem__(self, key, value):
        self.entities[key] = value

    def items(self):
        return self.entities.items()

def get_math_frame():
    result = _get_frame_title_dict()

    result['equation'] = _get_default_text_entity(
        text=r'$p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$',
        style='eng',
        x=h_center,
        y=RelativeY('eng_title', -230),
        size=18
    )

    result['chn_caption'] = _get_default_text_entity(
        text=r'正态分布',
        style='chn',
        x=h_center,
        y=frame_size[1] - 750,
        size=15
    )

    result['eng_caption'] = _get_default_text_entity(
        text='Normal Distribution',
        style='eng',
        x=h_center,
        y=RelativeY('chn_caption', -40),
        size=13
    )

    frame = Frame()
    frame.entities = result
    return frame


def get_two_column_chn_eng_frame_default_style():
    return {
        'left_right_margin' : 600,
        'mid_margin' : 30,
        'line_sep' : -50,
        'chn_size' : 15,
        'eng_size' : 13,
        'init_y_offset' : -200
    }

def get_two_column_chn_eng_frame(chn_title, eng_title, col1, col2, style):
    assert len(col1) == len(col2)
    result = _get_frame_title_dict()
    result['chn_title']['text'] = chn_title
    result['eng_title']['text'] = eng_title

    sideMargin = style['left_right_margin']
    midMargin = style['mid_margin']

    col1Left = sideMargin
    col1Right = h_center - midMargin
    col2Left = h_center + midMargin
    col2Right = frame_size[0] - sideMargin

    col1_x = (col1Left + col1Right) // 2
    col2_x = (col2Left + col2Right) // 2

    # put in the anchor entity
    result['col1_0'] = _get_default_text_entity(
        text=col1[0],
        style='chn',
        x=col1_x,
        y = RelativeY('eng_title', style['init_y_offset']),
        size=style['chn_size']
    )

    for i in range(1, len(col1)):
        entity_name = 'col1_{}'.format(i)
        result[entity_name] = _get_default_text_entity(
            text=col1[i],
            style='chn',
            x = col1_x,
            y = RelativeY('col1_{}'.format(i-1), style['line_sep']),
            size=style['chn_size']
        )

    for i in range(len(col2)):
        entity_name = 'col2_{}'.format(i)
        result[entity_name] = _get_default_text_entity(
            text=col2[i],
            style='eng',
            x = col2_x,
            y = RelativeY('col1_{}'.format(i), 0, 'center'),
            size=style['eng_size']
        )

    frame = Frame()
    frame.entities = result
    return frame




