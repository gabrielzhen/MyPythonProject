import os
for folderName,subfolders,filenames in os.walk('e:\\个人'):
    print('the current folder is'+folderName)
    for subfolder in subfolders:
        print(subfolder)
    for filename in filenames:
        print(filename)
    print('\n')

import zipfile,os
os.chdir('c:\\')
exampleZip=zipfile.ZipFile('example.zip')
exampleZip.namelist()
info=exampleZip.getinfo('sss.txt')
info.file_size
info.compress_size

newzip=zipfile.ZipFile('new.zip','w')
newzip.write('spam.txt',compress_type=)
newzip.close()