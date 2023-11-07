import os,shutil
folder='aaa'
abspath=os.path.abspath(folder)
filedir=os.path.dirname(abspath)
newfolder=os.path.join(filedir,'bbb')
if not os.path.exists(newfolder):
        os.makedirs(newfolder)
print(filedir)
print(newfolder)

for foldname,subfiles,filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.py'):
            print(os.path.join(foldname,filename))
            shutil.copy(os.path.join(foldname,filename),newfolder)
