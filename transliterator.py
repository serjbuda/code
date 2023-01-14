import string
import os
import shutil
path = '/Users/Сергій/Desktop/Trash/'
def trnasliterator(path):
    files = os.listdir(path)
    print(files)
    SYMBOLS = ".^`&()'~-,$%!@#;:+-*/\|?><={}[]абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS ={}
    for c, l in zip(SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    for file_name in files:
        split_tup = os.path.splitext(file_name)
        print(split_tup)
        p = split_tup[0].translate(TRANS)
        source = path + file_name
        destination = path + p + split_tup[1]
        os.rename(source, destination)
trnasliterator(path)
