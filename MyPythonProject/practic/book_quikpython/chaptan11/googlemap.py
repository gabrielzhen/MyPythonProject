import requests
res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
pyfile=open('cc.txt','wb')
for i in res.iter_content(1):#注意这里的使用方式
#for i in res.text[:255]:
    pyfile.write(i)
    #print(type(i))
    
pyfile.close()