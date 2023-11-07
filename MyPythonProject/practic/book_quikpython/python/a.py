alien={'x_position':0,'y_position':10,'speed':'mid'}

if alien['speed']=='low':
    x_inc=1
if alien['speed']=='mid':
    x_inc=2
if alien['speed']=='hig':
    x_inc=3

alien['x_position']=alien['x_position']+x_inc
for key,value in alien.items():
    print(key,end=' ')
    print(value)