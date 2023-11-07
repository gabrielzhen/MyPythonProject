import re
oldwords='The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
newfile=open('newwords.txt','w')
keywords=['ADJECTIVE','NOUN','ADVERB' ,'VERB']
for i in range(len(keywords)):
    rep=input('Enter an '+keywords[i]+':')
    comp=re.compile(keywords[i])
    oldwords=comp.sub(rep,oldwords)
newfile.write(oldwords)
newfile.close()