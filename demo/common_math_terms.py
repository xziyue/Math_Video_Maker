from source.quick_frame import *
from source.frame_exporter import export_all_frames
from source.get_root_dir import get_root_dir
import os

frames = []

frames.append(
    quick_title_frame('常见数学术语', r'\bfseries Common Mathematical Terms')
)

quick_section_marker('基本算术', 'Basic Arithmetic')

frames.append(quick_section_title_frame())

frames.append(
    quick_math_frame('加法', 'Addition',
                     '$a + b$',
                     '$a$加$b$',
                     '$a$ plus $b$')
)


frames.append(
    quick_math_frame('减法', 'Subtraction',
                     '$a - b$',
                     '$a$减$b$',
                     '$a$ minus $b$')
)

frames.append(
    quick_math_frame('乘法', 'Multiplication',
                     r'$a \times b \quad a \cdot b$',
                     '$a$乘$b$',
                     '$a$ times $b$')
)

frames.append(
    quick_math_frame('除法', 'Division',
                     r'$a \div b \quad a/b$',
                     '$a$除以$b$',
                     '$a$ divided by $b$')
)


frames.append(quick_two_column_chn_eng_frame('四则运算结果', 'Results of elementary arithmetic',
                                             ['和','差','积','商'],
                                           ['Sum', 'Difference', 'Product', 'Quotient']))


frames.append(
    quick_math_frame('正', 'Positive',
                     r'$+1$',
                     '正一',
                     'positive one')
)


frames.append(
    quick_math_frame('负', 'Negative',
                     r'$-1$',
                     '负一',
                     'Negative')
)


frames.append(
    quick_math_frame('正负', 'Plus-minus',
                     r'$\pm 1$',
                     '正负一',
                     'plus-minus one')
)

frames.append(
    quick_math_frame('整数', 'Integer',
                     r'$\mathbb{N} \subset \mathbb{Z}$',
                     '自然数是整数。',
                     'Natural numbers are integers.')
)

frames.append(
    quick_math_frame('小数', 'Decimal',
                     r'$1.23$',
                     '一点二三',
                     'one point two three')
)

frames.append(
    quick_math_frame('分数', 'Fraction',
                     r'\parbox{4cm}{$$\frac{22}{7}$$}',
                     '七分之二十二',
                     'twenty two over seven')
)




export_all_frames(frames, os.path.join(get_root_dir(), 'build'), True)

