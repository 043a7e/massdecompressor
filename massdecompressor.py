import os
import zipfile
import shutil

ctnumber = input('What is your CT or case number? ')
cdwcache = input('Drag your folder here: ')
ctloc, trash = os.path.split(cdwcache)
cdw = cdwcache.strip('\"' "\'")
ctfoldercache = str(ctloc) + '/' + ctnumber
ctfolder = ctfoldercache.strip('\"' "\'")
ctoriginals = ctfolder + '/_originals/'
ctdata = ctfolder + '/_data/'
zipsfolder = cdw + '/zips/'
os.mkdir(ctfolder)
os.mkdir(ctoriginals)
os.mkdir(ctdata)
os.mkdir(zipsfolder)

def decompressor():
    if file.endswith('.zip'):
        with zipfile.ZipFile(file, 'r') as topzip:
            topzip.extractall()
            zipend = zipsfolder + '/' + file
            os.rename(file , zipend)

def copyoriginals():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.zip'):
            originalend = ctoriginals + '/' + file
            shutil.copy2(file , originalend)

os.chdir(cdw)

for file in os.listdir(os.getcwd()):
    copyoriginals()
while any(file.endswith('.zip') for file in os.listdir(os.getcwd())):
    for file in os.listdir(os.getcwd()):
        decompressor()

shutil.rmtree(zipsfolder)
shutil.move(os.getcwd() , ctdata)
