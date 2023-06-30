
def user():
    showmau='''
    1.注册
    2.登录
    3.退出
    请选择编号动作
    '''
    print("aaa")
    choise=input(showmau) 
    while True:
        if choise=='3':
            break
        elif choise=='1':
            singup()
        elif choise=='2':
            singin()
        else:
            print('输入有误,重新选择')
            user()
user()