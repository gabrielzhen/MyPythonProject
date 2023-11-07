'''
passwords={'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog':'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import sys,pyperclip
if len(sys.argv)<2:
    print('usage:py pw.py[account] - copy account password')

account=sys.argv[1]

if account in passwords:
    pyperclip.copy
'''
''' 格式打印
def printpicnic(itemdict,leftwidth,rightwidth):
    print('PICNIC'.center(leftwidth+rightwidth,'-'))
    for k,v in itemdict.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth))
picnicitems={'sandwiches':4,'apple':6,'golds':100,'cookies':58}
printpicnic(picnicitems,13,5)
'''
'''copy
import pyperclip
pyperclip.copy('Hello ZhengTingjun')
pyperclip.paste()
'''
'''密码管理器
password={
    'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage:pw.py [account] -copy account password')
    sys.exit()
account=sys.argv[1]
if account in password:
    pyperclip.copy(password[account])
    print('the'+account+'copied to the clipboard')
else:
    print('please type the right account')
'''
import pyperclip
text=pyperclip.paste()
lines=text.split('\n')
for i in (len(lines)):
    lines[i]='*'+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
