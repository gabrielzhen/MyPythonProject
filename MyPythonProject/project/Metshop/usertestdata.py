from psutil import users
import pymysql
from faker import Faker
import random
import datetime

# 连接数据库
connection = pymysql.connect(
    host="192.168.6.156",  # 数据库主机地址
    user="root",  # 数据库用户名
    password="root",  # 数据库密码
    database="hexi"  # 数据库名称
)

cursor = connection.cursor()

# 初始化Faker对象
fake = Faker(['zh-CN'])

# 生成假数据
def generate_user(num_records=10):
    usersdata = []
    for i in range(1,num_records+1):
        username = fake.user_name()
        nickname = fake.first_name()
        pid = fake.uuid4()
        createtime = fake.date_time_this_decade(before_now=True, after_now=False)
        updatetime = createtime + datetime.timedelta(days=random.randint(1, 365))
        usersdata.append((i,username, nickname, pid, createtime, updatetime))
    return usersdata 

def generate_merchant(num_records=10):
    merchantdata = []
    for i in range(1,num_records+1):
        merchant= fake.company_prefix()
        phone = fake.phone_number()
        merchantdata.append((i,merchant,phone))
    return merchantdata

def generate_teainfo(numb=10):
    teainfo=[]
    for i in range(1,numb+1):
        teaname=fake.district()
        merchantid=random.choice(merchantdata)[0]
        teatypeid=random.choice([1,2,3,4])
        years=fake.year()
        season=fake.month_name()
        qty=random.choice([100,50,200,500])
        remark=fake.paragraph(nb_sentences=3,variable_nb_sentences=True)
        createrid=random.choice(userdata)[0]
        createtime = fake.date_time_this_decade(before_now=True, after_now=False)
        updatetime = createtime + datetime.timedelta(days=random.randint(1, 365))
        teainfo.append((i,teaname,merchantid,teatypeid,years,season,qty,remark,createrid,createtime,updatetime))
    return teainfo

def generate_toolinfo(numb=10):
    toolinfo=[]
    for i in range(1,numb+1):
        toolname=fake.job()
        merchantid=random.choice(merchantdata)[0]
        tooltype='陶瓷'
        remark=fake.paragraph(nb_sentences=3,variable_nb_sentences=True)
        createrid=random.choice(userdata)[0]
        createtime = fake.date_time_this_decade(before_now=True, after_now=False)
        updatetime = createtime + datetime.timedelta(days=random.randint(1, 365))
        toolinfo.append((i,toolname,merchantid,tooltype,remark,createrid,createtime,updatetime))
    return toolinfo

def generate_loginfo(numb=10):
    loginfo=[]
    for i in range(1,numb+1):
        logdate=fake.date(pattern='%Y-%m-%d',end_datetime=None)
        userid=random.choice(userdata)[0]
        teaid=random.choice([x[0] for x in teadata if x[8]== userid]) 
        toolid=random.choice([x[0] for x in toolinfo if x[5]==userid])
        title=fake.paragraph(nb_sentences=3,variable_nb_sentences=True)
        dryteasshap=fake.paragraph(nb_sentences=1,variable_nb_sentences=True)
        dryteassmell=fake.paragraph(nb_sentences=1,variable_nb_sentences=True)
        watertype='纯净水'
        createtime = fake.date_time_this_decade(before_now=True, after_now=False)
        updatetime = createtime + datetime.timedelta(days=random.randint(1, 365))
        loginfo.append((i,logdate,userid,teaid,toolid,title,dryteasshap,dryteassmell,watertype,createtime,updatetime))
    return loginfo


# 插入假数据
def insert_userdata(data):
    sql = """
    INSERT INTO userinfo (userid,username, nickname, pid, createtime, updatetime)
    VALUES (%s,%s, %s, %s, %s, %s)
    """
    cursor.executemany(sql, data)
    connection.commit()

def insert_merchant(data):
    sql='''
    insert into merchant(merchantid,merchant,phone) values (%s,%s,%s)'''
    cursor.executemany(sql,data)
    connection.commit()

def insert_teainfo(data):
    sql='''
    insert into teainfo(teaid,teaname,merchantid,teatypeid,years,season,qty,remark,createrid,createtime,updatetime) 
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.executemany(sql,data)
    connection.commit()

def insert_toolinfo(data):
    sql='''
    inert into toolinfo(toolid,toolname,merchantid,tooltype,remark,createrid,createtime,updatetime)
    values (%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.executemany(sql,data)
    connection.commit()

def insert_loginfo(data):
    sql='''
    insert into loginfo(logid,logdate,userid,teaid,toolid,title,dryteasshap,dryteassmell,watertype,createtime,updatetime)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.executemany(sql,data)
    connection.commit()
    

# # 用户数据
userdata= generate_user(2)
merchantdata =generate_merchant(20)
teadata=generate_teainfo(20)
toolinfo=generate_toolinfo(20)
loginfo=generate_loginfo(50)

insert_userdata(userdata)
insert_merchant(merchantdata)
insert_teainfo(teadata)
insert_toolinfo(toolinfo)
insert_loginfo(loginfo)
# 关闭连接
cursor.close()
connection.close()