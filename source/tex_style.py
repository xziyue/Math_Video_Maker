from source.get_root_dir import get_root_dir
import os

def get_english_style(data, fontsize=30):
    return r'''
\documentclass[border={0.5pt 0.5pt 0.5pt 0.5pt}]{standalone}
\usepackage[T1]{fontenc}
%%\usepackage{mathptmx}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\fontsize{%d}{%d}\selectfont
%s
\end{document}
''' % (fontsize, fontsize, data)


def get_chinese_style(data, fontpath, fontname, fontext, fontsize=30):
    return r'''
\documentclass[border={0.5pt 0.5pt 0.5pt 0.5pt}]{standalone}
\usepackage{xeCJK}
\usepackage{amsmath}
\usepackage{amssymb}
%%\setmainfont{STIX2Text-Regular.otf}
\setCJKmainfont[
Path=%s,
Extension=%s
]{%s}
\begin{document}
\fontsize{%d}{%d}\selectfont
%s
\end{document}
''' % (fontpath, fontext, fontname, fontsize, fontsize, data)

def get_chinese_style_kaiti(data, fontsize=30):
    rootFolder = get_root_dir()
    fontFolder = os.path.join(rootFolder, 'fonts')
    fontFilename = 'KaiTi_GB2312.ttf'
    fontname, fontext = os.path.splitext(fontFilename)
    assert os.path.exists(os.path.join(fontFolder, fontFilename))
    fontpath = fontFolder + os.path.sep
    return get_chinese_style(data, fontpath, fontname, fontext, fontsize)