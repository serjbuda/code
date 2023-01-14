import os, zipfile
import gzip
import tarfile
from os import walk
import sys
import shutil
import glob
path = r'/Users/Сергій/Desktop/Trash/'
def normalize(path):
    def folder_unpacker_cleaner(path):
        dirnames = next(walk(path), (None, [], None))[1]
        while len(dirnames)>0:
            subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
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
    def trnasliterator(path):
        files = os.listdir(path)
        SYMBOLS = "^`&()'~-,$%!@#;:+-*/\|?><={}[]абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        TRANSLATION = ("_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
        TRANS ={}
        for c, l in zip(SYMBOLS, TRANSLATION):
            TRANS[ord(c)] = l
            TRANS[ord(c.upper())] = l.upper()
        for file_name in files:
            split_tup = os.path.splitext(file_name)
            p = split_tup[0].translate(TRANS)
            source = path + file_name
            destination = path + p + split_tup[1]
            os.rename(source, destination)
    def sorter(path):
        names = os.listdir(path)
        folder_name = ['images','videos','documents','music','archives','unknown formats']
        for x in range(0,6):
            if not os.path.exists(path+folder_name[x]):
                os.makedirs(path+folder_name[x])
        for files in names:
            if '.png' in files and not os.path.exists(path+'images/'+files):
                shutil.move(path+files, path+'images/'+files)    
            elif '.jpg' in files and not os.path.exists(path+'images/'+files):
                shutil.move(path+files, path+'images/'+files)
            elif '.jpeg' in files and not os.path.exists(path+'images/'+files):
                shutil.move(path+files, path+'images/'+files)
            elif '.svg' in files and not os.path.exists(path+'images/'+files):
                shutil.move(path+files, path+'images/'+files)
            elif '.bmp' in files and not os.path.exists(path+'images/'+files):
                shutil.move(path+files, path+'images/'+files)
            elif '.avi' in files and not os.path.exists(path+'videos/'+files):
                shutil.move(path+files, path+'videos/'+files)
            elif '.mp4' in files and not os.path.exists(path+'videos/'+files):
                shutil.move(path+files, path+'videos/'+files)
            elif '.mov' in files and not os.path.exists(path+'videos/'+files):
                shutil.move(path+files, path+'videos/'+files)
            elif '.mkv' in files and not os.path.exists(path+'videos/'+files):
                shutil.move(path+files, path+'videos/'+files)
            elif '.doc' in files and not os.path.exists(path+'documents/'+files):
                shutil.move(path+files, path+'documents/'+files)
            elif '.docx' in files and not os.path.exists(path+'documents/'+files):
                shutil.move(path+files, path+'documents/'+files)
            elif '.txt' in files and not os.path.exists(path+'documents/'+files):
                shutil.move(path+files, path+'documents/'+files)
            elif '.pdf' in files and not os.path.exists(path+'documents/'+files):
                shutil.move(path+files, path+'documents/'+files)
            elif '.xlsx' in files and not os.path.exists(path+'documents/'+files):
                shutil.move(path+files, path+'documents/'+files)
            elif '.pptx' in files and not os.path.exists(path+'documents/'+files):
                shutil.move(path+files, path+'documents/'+files)
            elif '.mp3' in files and not os.path.exists(path+'music/'+files):
                shutil.move(path+files, path+'music/'+files)
            elif '.ogg' in files and not os.path.exists(path+'music/'+files):
                shutil.move(path+files, path+'music/'+files)
            elif '.wav' in files and not os.path.exists(path+'music/'+files):
                shutil.move(path+files, path+'music/'+files)
            elif '.amr' in files and not os.path.exists(path+'music/'+files):
                shutil.move(path+files, path+'music'+files)
            elif '.zip' in files and not os.path.exists(path+'archives/'+files):
                shutil.move(path+files, path+'archives/'+files)
            elif '.gz' in files and not os.path.exists(path+'archives/'+files):
                shutil.move(path+files, path+'archives/'+files)
            elif '.tar' in files and not os.path.exists(path+'archives/'+files):
                shutil.move(path+files, path+'archives/'+files)
            else:
                shutil.move(path+files, path+'unknown formats/'+files)
    def unarchiver(path):
        dir_name = path+'archives/'
        for item in os.listdir(dir_name):
            if item.endswith('.zip'):
                with zipfile.ZipFile(dir_name+item, 'r') as zip_ref:
                    if not os.path.exists(dir_name+item+' archive folder'):
                        os.mkdir(dir_name+item+' archive folder')
                        zip_ref.extractall(dir_name+item+' archive folder')
            elif item.endswith('.tar'):
                with tarfile.TarFile(dir_name+item, 'r') as tar_ref:
                    if not os.path.exists(dir_name+item+' archive folder'):
                        os.mkdir(dir_name+item+' archive folder')
                        tar_ref.extractall(dir_name+item+' archive folder')
            elif item.endswith('.gz'):
                with gzip.GzipFile(dir_name+item, 'r') as gz_ref:
                    if not os.path.exists(dir_name+item+' archive folder'):
                        os.mkdir(dir_name+item+' archive folder')
                        gz_ref.decompress(dir_name+item+' archive folder')
    folder_unpacker_cleaner(path)
    trnasliterator(path)
    sorter(path)
    unarchiver(path)
normalize(path)
