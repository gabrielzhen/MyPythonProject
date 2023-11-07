def connect(lists):
    lists[-1]='and'+' '+str(lists[-1])
    listname=','.join(lists)
    print(lists[-1])
    print(listname)

a=['sdf','dd1','3333']
a.app
connect(a)