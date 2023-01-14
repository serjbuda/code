import os
import shutil
path = '/Users/Сергій/Desktop/Trash/'
def normalize(path):
    #sort files to folders depending on its format
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
        elif 'images':
            continue
        elif 'documents':
            continue
        elif 'music':
            continue
        elif 'videos':
            continue
        elif 'documents':
            continue
        elif 'unknown formats':
            continue
        elif 'archives':
            continue
        else:
            shutil.move(path+files, path+'unknown formats/'+files)
normalize(path)
