#定义一个多入参函数
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last

    for key,value in user_info.items():
        profile[key]=value
    return profile

#输入参数
ztjprofile=build_profile('tingjun','zheng',location='chengdu',job='manager',salary='10000000$',health='very good',family='happy')

#输出
print(ztjprofile)