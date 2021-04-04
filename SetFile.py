import os
import shutil
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

cwd = folder_selected


def isDocument(file):
    docDir = "Documents"
    if not os.path.exists(docDir):
        os.makedirs(docDir)
    if file.endswith('.txt'):
        if not os.path.exists("Text Files"):
            dir = cwd + "/" + docDir + "/Text Files"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/Text Files/" + file)
        return True
    elif file.endswith('.pdf'):
        if not os.path.exists("pdf Files"):
            dir = cwd + "/" + docDir + "/pdf Files"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/pdf Files/" + file)
        return True
    elif file.endswith('.docx') or file.endswith('.doc'):
        if not os.path.exists("Word Files"):
            dir = cwd + "/" + docDir + "/Word Files"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/Word Files/" + file)
        return True
    elif file.endswith('.pptx') or file.endswith('.ppt'):
        if not os.path.exists("PPT Files"):
            dir = cwd + "/" + docDir + "/PPT Files"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/PPT Files/" + file)
        return True
    else:
        return False


def isMedia(file):
    docDir = "Media"
    if not os.path.exists(docDir):
        os.makedirs(docDir)
    if file.endswith('.mp3'):
        if not os.path.exists("Songs"):
            dir = cwd + "/" + docDir + "/Songs"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/Songs/" + file)
        return True
    elif file.endswith('.mp4'):
        if not os.path.exists("Vedio"):
            dir = cwd + "/" + docDir + "/Vedio"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/Vedio/" + file)
        return True
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        if not os.path.exists("Picture"):
            dir = cwd + "/" + docDir + "/Picture"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/Picture/" + file)
        return True
    else:
        return False


def isProgram(file):
    docDir = "Program"
    if not os.path.exists(docDir):
        os.makedirs(docDir)
    if file.endswith('.exe'):
        if not os.path.exists("Executable"):
            dir = cwd + "/" + docDir + "/Executable"
            if not os.path.exists(dir):
                os.makedirs(dir)
        shutil.move(cwd + "/" + file, cwd + "/" + docDir + "/Executable/" + file)
        return True
    else:
        return False


for root, dirs, files in os.walk(cwd, topdown=True):
    dirs.clear()  # with topdown true, this will prevent walk from going into subs
    for file in files:

        if isMedia(file):
            continue
        elif isDocument(file):
            continue
        elif isProgram(file):
            continue
        print(file)
