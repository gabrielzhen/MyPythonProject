import os
file=open('makeTextFile.py')
linnum=0
for x in file.readlines():
    print(x)
    linnum+=1
    if linnum%5==0:
        input('countitnue...')
        continue