import os
from os import walk
import sys
import shutil
import glob
path = r'/Users/Сергій/Desktop/Trash/'
def normalize(path):
    def unpacker(path):
        dirnames = next(walk(path), (None, [], None))[1]
        print(dirnames)
        while len(dirnames)>0:
            subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
            print(subfolders)
            for sub in subfolders:
                for f in os.listdir(sub):
                    src = os.path.join(sub, f)
                    dst = os.path.join(path, f)
                    shutil.move(src, dst)
            folders = list(os.walk(path))[1:]
            for folder in folders:
                if not folder[2]:
                    os.rmdir(folder[0])
            dirnames = next(walk(path), (None, [], None))[1]
            print(len(dirnames))
    unpacker(path)
normalize(path)
