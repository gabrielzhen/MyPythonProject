#!/user/bin/env python
'make file and import file'
import os

while True:
    filename=input('please entr the files name')
    if os.path.exists(filename):
        print(f'already exists file {filename},please enter other one')
    else:
        break
        
all=[]
print('now enter the content,use . to exit')
while True:
    entry=input('>')
    if entry=='.':
        break
    else:
        all.append(entry)
        
with open(filename,'w') as f:
    for i in all:
        f.write(i+'\n')