from source.quick_frame import *
from source.frame_exporter import export_all_frames
from source.get_root_dir import get_root_dir
import os

frames = []

frames.append(
    quick_title_frame('常见数学术语', r'\bfseries Common Mathematical Terms')
)

chnTitle = '基本算术'
engTitle = 'Basic Arithmetic'

quick_section_marker(chnTitle, engTitle)
frames.append(quick_section_title_frame())
quick_section_marker(None, None)

frames.append(
    quick_two_column_chn_eng_frame(chnTitle, engTitle,
                                    ['加法','减法','乘法','除法'],
                                    ['Addition', 'Subtraction', 'Multiplication', 'Division'])
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     '$a + b$',
                     '$a$加$b$',
                     '$a$ plus $b$')
)


frames.append(
    quick_math_frame(chnTitle, engTitle,
                     '$a - b$',
                     '$a$减$b$',
                     '$a$ minus $b$')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$a \times b \quad a \cdot b$',
                     '$a$乘$b$',
                     '$a$ times $b$')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$a \div b \quad a/b$',
                     '$a$除以$b$',
                     '$a$ divided by $b$')
)


frames.append(quick_two_column_chn_eng_frame(chnTitle, engTitle,
                                             ['和','差','积','商', '余数'],
                                           ['Sum', 'Difference', 'Product', 'Quotient', 'Remainder']))


frames.append(quick_three_column_eng_chn_eng_frame(chnTitle, engTitle,
                                                   ['$+$', '$-$', '$\pm$'],
                                                   ['正', '负', '正负'],
                                                   ['Positive', 'Negative', 'Plus-minus']
                                                   ))

frames.append(quick_two_column_chn_eng_frame(chnTitle, engTitle,
                                             ['整数','小数','分数','真分数', '假分数', '带分数'],
                                           ['Integer', 'Decimal', 'Fraction', 'Proper fraction', 'Improper fraction', 'Mixed fraction']
                                             ))

frames.append(
quick_two_column_chn_eng_frame(chnTitle, engTitle,
                                             ['相反数','倒数'],
                                           ['Opposite', 'Reciprocal']
                                             )
)


frames.append(
quick_two_column_chn_eng_frame(chnTitle, engTitle,
                                             ['幂', '开方', '对数', '自然对数'],
                                           ['Exponentiation', 'Root', 'Logarithm', 'Natural logarithm']
                                             )
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$a^2$',
                     '$a$的平方',
                     '$a$ squared')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$a^3$',
                     '$a$的立方',
                     '$a$ cubed')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$a^n$',
                     '$a$的$n$次方',
                     r'\parbox{6cm}{\centering $a$ raised to the power of $n$\\ \centering $a$ to the $n$}')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$\sqrt{a}$',
                     '$a$的平方根',
                     'square root of $a$')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$\sqrt[3]{a}$',
                     '$a$的立方根',
                     'cube root of $a$')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$\sqrt[n]{a}$',
                     '$a$的$n$次方根',
                     r'$n$-th root of $a$')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$\log a$',
                     '$a$的对数',
                     r'\emph{log} $a$')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$\log_b a$',
                     '以$b$为底的$a$的对数',
                     r'\parbox{6cm}{\centering the logarithm of $a$ to the base $b$\\ \centering the log, base $b$, of $a$}')
)

frames.append(
    quick_math_frame(chnTitle, engTitle,
                     r'$\ln a$',
                     '$a$的自然对数',
                     r'\emph{ell-enn} $a$')
)

export_all_frames(frames, os.path.join(get_root_dir(), 'build'), True)

