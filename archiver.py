import os, zipfile
from zipfile import ZipFile
import gzip
import tarfile
from os import walk
import sys
import shutil
import glob
path = r'/Users/Сергій/Desktop/Trash/'
def normalize(path):
    def unarchiver(path):
        dir_name = path+'archives/'
        for item in os.listdir(dir_name):
            if item.endswith('.zip'):
                with zipfile.ZipFile(dir_name+item, 'r') as zip_ref:
                    zip_ref.extractall(dir_name)
            elif item.endswith('.tar'):
                with tarfile.TarFile(dir_name+item, 'r') as tar_ref:
                    tar_ref.extractall(dir_name)
            elif item.endswith('.gz'):
                with gzip.GzipFile(dir_name+item, 'r') as gz_ref:
                    gz_ref.decompress(dir_name)
    unarchiver(path)
normalize(path)
