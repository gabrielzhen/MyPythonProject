import pandas as pd
from sqlalchemy import create_engine

db_url='mysql+pymysql://root:pisen1@192.168.6.115:9030/Pisen_DW'
engin=create_engine(db_url)

material_list=pd.read_sql('''select dmmv.FNUMBER goodsCode,sum(a.FREALQTY) qty
from Pisen_DW.DWD_SAL_OUT a
left join DIM_customer_master_v dcmv  on a.FCUSTOMERNBR =dcmv.FNUMBER 
left join DIM_material_master_v dmmv  on a.FMATERIALNBR  =dmmv.FNUMBER 
left join DIM_TIME dt on a.FDATE =dt.id 
where year ='2024' and month >='3' and SALETYPE not in ('电商入仓','线上直营') 
and dmmv.FCATEGORY like '产成品%%' and dmmv.FCATEGORY <> '产成品-其他类'
group by dmmv.FNUMBER ,dmmv.FNAME ,dmmv.FCATEGORY
order by sum(a.FREALQTY) desc
limit 1''',engin)

box_rul=pd.read_excel('箱规.xlsx')

material_box=pd.merge(material_list,box_rul)
# print(material_box)

def best_boxrul(goodscode,lim):
    params=(goodscode,lim)
    qty_list=pd.read_sql('''select a.FREALQTY fqty,count(a.FBILLNO) orders
from Pisen_DW.DWD_SAL_OUT a
left join DIM_customer_master_v dcmv  on a.FCUSTOMERNBR =dcmv.FNUMBER 
left join DIM_material_master_v dmmv  on a.FMATERIALNBR  =dmmv.FNUMBER 
left join DIM_TIME dt on a.FDATE =dt.id 
where dt.year ='2024' and dt.month >=1 and SALETYPE not in ('电商入仓','线上直营') and dmmv.FNUMBER=%s and a.FREALQTY<%s
group by a.FREALQTY
order by a.FREALQTY''',engin,params=params)
    # qty_list['shang']=qty_list['fqty']//35
    # qty_list['yu']=qty_list['fqty']%35
    # qty_list['b']=qty_list['fqty']*qty_list['orders']
    # qty_list['c']=(qty_list['shang']+qty_list['yu'])*qty_list['orders']
    # qty_list.loc['合计']=qty_list[['b','c']].sum(axis=0)
    # print(qty_list)

    comb=[]
    for i in range(0,lim,10):
        if i==0:
            qty_list['b']=qty_list['fqty']*qty_list['orders']
            comb.append({'code':goodscode,'box':i,'c':qty_list['b'].sum()})
        else:
            qty_list['shang']=qty_list['fqty']//i
            qty_list['yu']=qty_list['fqty']%i
            qty_list['c']=(qty_list['shang']+qty_list['yu'])*qty_list['orders']
            comb.append({'code':goodscode,'box':i,'c':qty_list['c'].sum()})
    return min(comb,key=lambda x:x['c'])

# best_boxrul('031160203037',50)

lists={'goodsCode':[],'box':[],'sore':[]}
for row in material_box.iterrows():
    r=best_boxrul(row[1]['goodsCode'],int(row[1]['smallbox']))
    lists['goodsCode'].append(r['code'])
    lists['box'].append(r['box'])
    lists['sore'].append(r['c'])
final=pd.merge(material_box,pd.DataFrame(lists))
final['goodsCode']=final['goodsCode'].apply(str)+'\t'
print(final)
# final.to_csv('final.csv',encoding='utf8')