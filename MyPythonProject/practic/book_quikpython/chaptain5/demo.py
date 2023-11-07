''' 字典的初步应用
spam={'name':'zhengtingjun','age':'33'}
print(spam['name']+' '+spam['age'])
'''
'''字典默认值方法的使用，字典计数
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count={}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1

pprint.pprint(count)
'''
allguests={'Alice':{'apple':5,'pretzels':12},
'Bob':{'ham sndwiches':3,'apple':2},
'Carol':{'cups':3,'apple pies':1}}
def totalBrougt(guests,item):
    numBrougt=0
    for i,j in guests.items():
        numBrougt+=j.get(item,0)
    return numBrougt
print(totalBrougt(allguests,'apple'))