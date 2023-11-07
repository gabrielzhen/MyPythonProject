import shutil,os,re
#todo:find amrican type
dateformat=re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""",re.VERBOSE)
#todo:list folder to find 
for i in os.listdir():
    sea=dateformat.search(i)
    if sea==None:
        continue
    else:
        beforepart=sea.group(1)
        monthpart=sea.group(2)
        daypart=sea.group(4)
        yearpart=sea.group(6)
        afterpart=sea.group(8)
#todo:change the type
        abspath=os.path.abspath('.')
        oldfile=os.path.join(sbapath,i)
        eurofilename=beforepart+daypart+monthpart+yearpart+afterpart
        newfile=os.path.join(abspath,eurofilename)

        shutil.move(oldfile,newfile)

