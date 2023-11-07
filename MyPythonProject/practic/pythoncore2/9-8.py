m=input('put the mudule name')
mud=dir(__import__(m))
for i in mud:
    print('%s加%s加%s',i,type(getattr(__import__(m),i)))

