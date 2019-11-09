import os

def get_root_dir():
    myFilename = os.path.abspath(__file__)
    myFolder, _ = os.path.split(myFilename)
    rootFolder, _ = os.path.split(myFolder)
    return rootFolder