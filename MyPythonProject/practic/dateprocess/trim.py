#利用切片来实现trim函数的功能
#思想：利用循环判断,并且注意''的判断
def trim(s):
    i=0
    j=-1
    c=len(s)+1
    if s!='' :
        while s[i]==' ' and len(s[i:])>1:
            i+=1
        while s[j]==' ' and len(s[:j])>1:
            j-=1
        print(i,c+j,len(s[i:c+j]),s[i:c+j])
        return s[i:c+j]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')