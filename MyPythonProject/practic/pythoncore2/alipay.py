import pandas,os
import cx_Oracle

dir='E:\\工作\\工作项目\\IPO审计相关\\23年\\支付宝流水匹配\\2023年支付宝流水\\'
testdir='E:\\工作\\工作项目\\IPO审计相关\\23年\\支付宝流水匹配\\2023年支付宝流水\\2023.4月\\20230401_2088301451669120\\'
dsn = cx_Oracle.makedsn(host='192.168.6.19', port=1521, sid='easdbfir')
conn = cx_Oracle.connect(user='tmp', password='pisen', dsn=dsn)
for root,dir,files in os.walk(dir):
    for f in files:
        if f.endswith('账务明细.csv'):
            print(os.path.join(root,f))
            df=pandas.read_csv(os.path.join(root,f),skiprows=4,comment='#',encoding='GB18030')
            df = df.astype(str).where(df.notnull(), None)
            cursor=conn.cursor()
            query=f'insert into ipo_alipay_2023 values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15)'
            cursor.executemany(query, df.values.tolist())
            conn.commit()
            cursor.close()
conn.close()


