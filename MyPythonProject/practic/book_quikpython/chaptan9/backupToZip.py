import zipfile,os
#todo:输入参数指定文件夹
def backupToZip(folder):
    num=1
    while True:
        zipfilename=folder+'_'+str(num)+'.zip'
        paths=os.path.abspath(zipfilename)
        if not os.path.exists(paths):
            break
        num+=1
    print(zipfilename)

#todo:创建zip文件
    bakupfile=zipfile.ZipFile(zipfilename,'w')
#todo:遍历文件夹文件并添加到zip
    for foldername,subfolder,filename in os.walk(folder):
        print('Adding file in %s..'%(foldername))
        bakupfile.write(foldername)
        for filenames in filename:
            bakupfile.write(os.path.join(foldername,filenames))
    bakupfile.close()

backupToZip('aaa')
