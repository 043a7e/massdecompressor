import os
import zipfile
import shutil

ctnumber = input('What is your CT or case number? ')
cdwcache = input('Drag your folder here: ')
cdw = cdwcache.strip('\"' "\'")
ctloc, trash = os.path.split(cdw)
ctfoldercache = str(ctloc) + '/' + ctnumber
ctfolder = ctfoldercache.strip('\"' "\'")
ctoriginals = ctfolder + '/_originals/'
ctdata = ctfolder + '/_data/'
zipsfolder = cdw + '/zips/'
os.mkdir(ctfolder)
os.mkdir(ctoriginals)
os.mkdir(ctdata)

def decompressor():
    os.mkdir(zipsfolder)
    for file in os.listdir(os.getcwd()):
        print('Decompressing ' + file)
        if file.endswith('.zip'):
            with zipfile.ZipFile(file, 'r') as topzip:
                topzip.extractall()
                topzip.close()
                zipend = zipsfolder + '/' + file
                os.rename(file , zipend)
        else:
            continue

def copyoriginals():
    print('Moving ' + file)
    originalend = ctoriginals + '/' + file
    shutil.copy2(file , originalend)

        
os.chdir(cdw)

for file in os.listdir('.'):
    copyoriginals()
while any(file.endswith('.zip') for file in os.listdir('.')):
    decompressor()

shutil.rmtree(zipsfolder)
shutil.move(os.getcwd() , ctdata)
