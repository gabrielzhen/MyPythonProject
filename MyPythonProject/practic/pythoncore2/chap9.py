#m = input('输入模块名: ')
#module = __import__(m)
#ml = dir(module)
## print(ml)
#for i in ml:
#    print('name: ', i)
#    print('type: ', type(getattr(module,i)))
#    print('value: ', getattr(module,i))
#    print('')

#  import os
#  dir='C:\\Users\\Pisen\\AppData\\Local\\Programs\\Python\\Python310\\lib\\'
#  files=[f for f in os.listdir(os.path.abspath(dir)) if f.endswith('.py')]
#  for file in files:
#      fulldir=os.path.join(dir,file)
#      with open(fulldir,'r') as f:
#          if f.read() 
#  
'''
家庭理财。创建一个家庭理财程序。你的程序需要处理储蓄、支票、金融市场，定期存款等多种账户。
为每种账户提供一个菜单操作界面，要有存款、取款、借、贷等操作。另外还要提供一个取消操作选项。
用户退出这个程序时相关数据应该保存到文件里去（出于备份的目的，程序执行过程中也要备份
'''
#import os,json
##todo1定义一个用户类 实现注册 删除 登录
#class Person:
#    def singup(self):
#        ID=input('输入注册用户')
#        userfile='%s.json'%ID
#        if userfile in os.listdir(os.getcwd()):
#            print('用户已经存在')
#        else:
#            name=input('请输入新的用户名：')
#            pawd=input('请输入新用户密码：')
#            regest_user={}
#            regest_user['name']=name
#            regest_user['password']=pawd
#            regest_user['yuer']=0
#            regest_user['jiekuan']=0
#            regest_user['daikuan']=0
#            userfile=open(userfile,'w')
#            json.dump(regest_user,userfile)
#            userfile.close()
#            print('注册成功')
#            self.user()
#                
#    def singin(self):
#        ID=input('登录用户名输入：')
#        file='%s.json'%ID
#        if file in os.listdir(os.getcwd()):
#            with open(file,'r') as f:
#                user_direct=json.load(f)
#            pswd=input('输入登录密码：')
#            if pswd==user_direct['password']:
#                print('登录成功')
#                print(user_direct)
#            else:
#                print('密码错误重新登录')
#        else:
#            print('输入有误请重新输入')
#
#    def user(self):
#        showmau='''
#        1.注册
#        2.登录
#        3.退出
#        请选择编号动作
#        '''
#        print("aaa")
#        choise=input(showmau) 
#        while True:
#            if choise=='3':
#                break
#            elif choise=='1':
#                self.singup()
#            elif choise=='2':
#                self.singin()
#            else:
#                print('输入有误,重新选择')
##todo2定义一个账户类 实现每个账户类型的存取借贷
#
##todo3定义一个保存方法
#
#if __name__=='__main__':
#    persion=Person()
#    persion.user()
'''
9-11.Web站点地址。

    a) 编写一个URL.书签管理程序。使用基于文本的菜单，用户可以添加、修改或者删除书签数据项、书签数据项中包含站点的名称、URL地址和一行简单说明（可选）。另外提供检索功能，可以根据检索关键字在站点名称和URL两部分查找可能的匹配。程序退出时把数据保存到一个磁盘文件中去；再次执行的时候加载保存的数据。

    b) 改进a)的解决方案，把书签输出到一个合法且语法正确的HTML文件（.html或htm）中，这样用户就可以使用浏览器查看自己的书签清单。另外提供创建“文件夹”功能，对相关的书签进行分组管理。

    附加题：请阅读Python的re模块了解有关正则表达式的资料，使用正则表达式对用户输入的URL进行验证。

'''
#todo1编写一个文本标签管理类包括新增 修改 删除 查找功能并 保存，保存的事后可以利用参数获得文件夹管理功能
#def add(self):
#    title=input('输入title')
#    url=input('输入url')
#    
#
#def modify(self):
#    pass
#
#def delete(self):
#    pass
#
#def search()
##todo2更具文件生成一个html文件并展示