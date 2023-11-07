# import time,string

# userdir={'ztj':['123',1]}
# #login 1.显示上次登录时间 2.不超过4小时显示 3用户名不区分大小写 4.不容许符号和空白字符
# reg_table=string.ascii_letters+string.digits

# def checkname(name):
#     for n in name:
#         if n not in reg_table:
#             print('illegal username')
#             return False
#         return True 

# def login():
#     name=input("please input the login name:")
#     while True:
#         if checkname(name)==False:
#             continue
#         if name.lower() in userdir:
#             paswd=input('password please:')
#             if paswd==userdir[name.lower()][0]:
#                 print('welcome',name.lower())
#                 userdir[name.lower()][-1]=time.time()
#                 return
#             else:
#                 print('error user')
                
            
# if __name__=='__main__':
#     login()
#manage 1.删除一个用户 显示系统中所有名字和密码
db={}
def add():
    name=input('input name:')
    id=input('input id:')
    if name in db:
        print("exists")
    db[name]=id

def show():
    for name in sorted(db.keys()):
        print(name,db[name])

def show_id():
    new_dict={v:k for k,v in db.items()}
    for id in sorted(new_dict.keys()):
        print(new_dict[id],id)

def menu():
    prompt='''
    add:a
    show_name:n
    show_id:i
'''
    while True:
        choise=input(prompt)
        if choise == 'a':add()
        if choise == 'n':show()
        if choise == 'i':show_id()
if __name__ == '__main__':
    menu()