'''read and write file
try:
	f=open('../READM.md','r')
	print(f.read())
finally:
	if f:
		f.close()

with open('../README.md','r') as f:
	print(f.read())
	
f=open('../README.md','w')
f.write('abc')
f.close()
'''
'''memary read and write
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
b=StringIO('i am gold')
#print(f.getvalue())
print(f.readline())
print(b.readline())
'''
import os
print(os.path.abspath('.'))#pwd
a=[x for x in os.listdir('.')
 if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']#list local fold's file
print(a)
