import subprocess
import os
import random
import string
import sys
from skimage import io
import codecs

def _get_random_filename(length=15):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def _tex_cleanup(tempName):
    suffices = ['aux', 'log', 'tex']
    for suffix in suffices:
        filename = tempName + '.' + suffix
        if os.path.exists(filename):
            os.remove(filename)

def _call_tex(target, texData):
    # write data to temp file
    tempName = _get_random_filename()
    tempFilename = tempName + '.tex'
    tempPDFFilename = tempName + '.pdf'
    tempPNGFilename = tempName + '.png'

    with codecs.open(tempFilename, 'w', 'utf8') as outfile:
        outfile.write(texData)

    #print(texData)

    # generate pdf first
    output = None
    try:
        output = subprocess.Popen(
            [target, '-interaction=nonstopmode', '--shell-escape', tempFilename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output.wait()
        #output = subprocess.run([target, '-interaction=nonstopmode', '--shell-escape', tempFilename], check=True, stderr=subprocess.PIPE)
    except Exception as e:
        print('unable to create process: \n', e, file=sys.stderr)


    if output.returncode != 0:
        print(f'{target} exited with error code {output.returncode}', file=sys.stderr)
        print('latex output: \n', output.stdout.read().decode('latin-1'))
    my_stderr_data = output.stderr.read().decode('latin-1')
    if len(my_stderr_data) > 0:
        print('stderr from latex: \n', my_stderr_data, file=sys.stderr)

    _tex_cleanup(tempName)

    # check if the pdf exists
    if not os.path.exists(tempPDFFilename):
        return None

    # convert pdf to png
    try:
        output = subprocess.run(['convert', '-density', '350',
                                 #'-border', '1',
                                 tempPDFFilename, '-colorspace', 'RGB', tempPNGFilename],
                                check=True, stderr=subprocess.PIPE)
        my_stderr_data = output.stderr.decode('latin-1')
        if len(my_stderr_data) > 0:
            print('error message from convert: \n', my_stderr_data, file=sys.stderr)
    except Exception as e:
        print('error occurred when calling convert: \n', e, file=sys.stderr)

    os.remove(tempPDFFilename)

    img = None
    if os.path.exists(tempPNGFilename):
        img = io.imread(tempPNGFilename)
        os.remove(tempPNGFilename)

    return img


def render_pdflatex(texData):
    return _call_tex('pdflatex', texData)

def render_xelatex(texData):
    return _call_tex('xelatex', texData)