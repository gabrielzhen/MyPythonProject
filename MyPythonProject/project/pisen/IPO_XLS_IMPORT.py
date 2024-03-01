import os
import pandas as pd
from sqlalchemy import create_engine,Float
import cx_Oracle
#1.数据库配置 文件路径
folder='E:\\工作\\23年整理\\工作项目\\IPO审计相关\\23年\\支付宝流水匹配\\2023年7.12月支付宝流水\\2023.12月'
#folder='E:\\20230101_2088301451669120'
database_add='192.168.6.19'
database_user='tmp'
database_pass='pisen'
database_name='easdbfir'
table_name='ct_cus_cerp_tmzfb2023_ALL'
file_sk=4


file_foot_sk=4
chunk_size=10000
#数据类型转化:
convert_dict={
'账务流水号':str,
  '业务流水号':str,
  '商户订单号':str,
  '商品名称':str,
  '发生时间':str,
  '对方账号':str,
  "收入金额（+元）" :str,
  "支出金额（-元）" :str,
  '账户余额（元）':str,
  '交易渠道':str,
  '业务类型':str,
  '备注':str,
  '业务基础订单号':str,
  '业务订单号':str,
  '业务描述':str,
  '表名':str
}
#2.遍历文件获取有效的文件路径列表
engine=create_engine(f'oracle+cx_oracle://{database_user}:{database_pass}@{database_add}/?service_name=easdbfir')
cx_conn=cx_Oracle.connect(f'{database_user}/{database_pass}@{database_add}:1521/{database_name}')

for root,dirs,files in os.walk(folder):
    for file_name in files:
        if file_name.endswith('账务明细.csv'):
            file_path=os.path.join(root,file_name)
            print(file_path)
            df=pd.read_csv(file_path,encoding='GBK',skiprows=4,skipfooter=4,encoding_errors='ignore')
            df['表名']=file_name
            # df=df.select_dtypes(include=['Float64']).astype('str')
            # df["收入金额（+元）"]= df["收入金额（+元）"].astype('str')#.with_variant(Float(precision=53), 'oracle')
            # df["支出金额（-元）"]= df["支出金额（-元）"].astype('str')#.with_variant(Float(precision=53), 'oracle')
            # df["账户余额（元）"]= df["账户余额（元）"].astype('str')#.with_variant(Float(precision=53), 'oracle')
            df=df.astype(convert_dict)
            print(len(df))
            data=df.values.tolist()
            cursor=cx_conn.cursor()
            try:
                placeholders=','.join([':'+str(i+1) for i in range(len(df.columns))])
                sql=f'insert into {table_name} values ({placeholders})'
                cursor.executemany(sql,data)
                cx_conn.commit()
            except Exception as e:
                cx_conn.rollback()
                print('Error',e)
            finally:
                cursor.close()
            # for i in range(0,len(df),chunk_size):
            #     chunk=df.iloc[i:i+chunk_size]
            #     chunk.to_sql(table_name,engine,index=False,if_exists='append')


