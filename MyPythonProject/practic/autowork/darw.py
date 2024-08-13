import seaborn as sns
import matplotlib.pyplot as plt
import pandas,pymysql,sys,json
from pandas import Series,DataFrame

conn=pymysql.connect(
    host = '192.168.6.115',
    port=9030,
    user='admin',
    password='pisen1',
    database='Pisen_DW'
)

query=f'''
               with sale as (
	select a.matnumber,sum(a.amount) amount,sum(a.fqty) fqty
	from 
	DWS_MANAGE_SALE_MONTH_V2 a
	left join DIM_customer_master_v dcmv  on a.cusnumber =dcmv.FNUMBER 
	where  fmonth <=6 and fyear in ('2023')
	and SALETYPE not in ('电商入仓','线上直营')
	group by a.matnumber
	)
	select fprice,count(1) count,sum(fqty) fqty from (
	select is_more, FNUMBER,FNAME,FPRICE,ifnull(fqty,0) fqty,ifnull(amount,0) amount,sum(amount)over(order by amount desc) leiji
	from 
	(
	select dmmv.IS_MORE,dmmv.FMANULCLASS,dmmv.FNUMBER ,dmmv.FNAME ,b.FPRICE,sum(a.amount) amount,sum(a.fqty) fqty,
	round(sum(a.amount)/sum(a.fqty),2) per
	from DIM_MATERIAL_BIGPRICE b
	left join DIM_material_master_v dmmv  on b.FNUMBER =dmmv.FNUMBER 
	left join sale a on a.matnumber =b.FNUMBER
	where dmmv.FMANULCLASS like '{sys.argv[1]}'
	group by dmmv.IS_MORE,dmmv.FMANULCLASS,dmmv.FNUMBER ,dmmv.FNAME ,b.FPRICE
	) a -- where abs(fprice-ifnull(per,fprice))<10 -- 取消销售价格和产品单价差距过大的产品 疑似促销活动
	) a group by fprice order by fprice'''

pd=pandas.read_sql(query,conn)
conn.close()
pd['fprice']=pd['fprice']//int(sys.argv[2])*int(sys.argv[2])
pd['fprice']=pd['fprice'].astype(int)
print(pd.dtypes)
print(pd.groupby('fprice').sum())
sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)
sns.barplot(x='fprice',y='fqty',data=pd)
lists2={'aa':[1,2,3],'bb':[4,6,7]}
s1=Series(lists2)
s2=Series(data=lists2,index=['aa','bb','cc'])
d1=DataFrame(lists2)
d2=DataFrame(data=lists2,index=['a','b','c'])
print(s1)
print(s2)
print(d2)
print(d2.describe())
df1=DataFrame({'name':['ZhangFei','GuanYu','a','b','c'],'data1':range(5)})
df2=DataFrame({'name':['ZhangFei','GuanYu','A','B','C'],'data2':range(5)})
df3=pandas.merge(df1,df2,how='outer')
print(df1)
print(df2)
print(df3)

jsondata='{"a":1,"b":2}'
print(json.loads(jsondata))