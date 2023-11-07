'''
spam=['a', 'b', 'c', 'd']
a=spam*3
print(a)
'''
spam=['apple','bananas','tofu','cats']
a=''
for i in spam:
    if i==spam[-1]:
        a=a+'and '+i
    else:
        a=a+i+','
print(a)