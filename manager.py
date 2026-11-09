import os
import shutil


def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def deleteFolder(path):
    empty=True
    for item in os.listdir(path):
        empty=False
    if not empty:
     print("לא ריק ")
    else:
        shutil.rmtree(path, ignore_errors=True)

def createFile(path):
    if not os.path.exists(path):
        open(path, 'w').close()

def writeFile(path, content):
    with open(path, 'w') as f:
        f.write(content)
def deleteFile(path):
    if os.path.exists(path):
        os.remove(path)

def readFolder(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
           print(f.read())

def readDyrectory(path):
 if os.path.exists(path):
     print(path)









