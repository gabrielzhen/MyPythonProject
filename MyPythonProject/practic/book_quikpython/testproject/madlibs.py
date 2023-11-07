import sys,re
madlibs=open('.\\madlibs.txt','w')
madlibs.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
madlibs.close()

readlibs=open('.\\madlibs.txt')
content=readlibs.read()
print(content)
readlibs.close()

searchlist=['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for slist in searchlist:
    inputword=input('input the word you wanted'+slist)
    print(content)
    regeword=re.compile(slist)
    content=regeword.sub(inputword,content)
    print(content)
replopen=open('.\\madlibs.txt','w')
ddd=replopen.write(content)
replopen.close()

readlibs=open('.\\madlibs.txt')
content=readlibs.read()
print(content)
readlibs.close()

