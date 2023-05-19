print('next str test')
x='ztj'
print('first %s',id(x))
x='gyf'
print('first %s',id(x))
print('next number test')
for i in range(10):
    x=i
    print('first %s',id(i))
    print('first %s' % id(x),1) 
