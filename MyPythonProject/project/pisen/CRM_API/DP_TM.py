#目的:使用接口自动对接平台店铺信息，只获取最近更新日期一月之内的数据
#1.从接口获取相关数据（字段信息）
#2.写入数据库具体表中（文本文件中）

import requests,pymysql
import json,csv
from datetime import datetime,timedelta

def fetch_data(page_size, page_index):
    url = "https://mingdao.yunma99.com/api/v2/open/worksheet/getFilterRows"
    from_day=datetime.now()-timedelta(days=15)
    yestoday=from_day.strftime('%Y-%m-%d')

    payload = json.dumps({
        "appKey": "9eb44cd3fc1e56b5",
        "sign": "NmMwNGQ3NDA0ODQ4OTkyYjk4YTNlYmUzZWNjNzU4MmU3NGVhMTNhZGU0ZmMzOGE0YTYyOWU3Mjc0MWYyM2Y0NA==",
        "worksheetId": "65af9a78a73e46396661f694",
        "viewId": "66616b00c84bb1e76fa84d73",
        "pageSize": page_size,  # 使用传入的 page_size 参数
        "pageIndex": page_index,  # 可选的 page_index 参数
        "listType": 0,
        "filters": [
            {
                "controlId": "utime",
                "dataType": 15,
                "spliceType": 1,
                "filterType": 14,
                "value": yestoday
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data=json.loads(response.text)["data"]
    rows=[]
    if len(data["rows"])!=0:
        for row in data["rows"]:
            
            metrow=[
            '饿了么店铺',
            row.get("659f9bcba256f71f993ca188"),
            row.get("659e02cfa256f71f993c9ca6"),
            row.get("66040124896e647b38f444f1"),
            row.get("66176f965822c79db4dd5209"),
            row.get("66176f965822c79db4dd5206"),
            row.get("66176f965822c79db4dd5207"),
            row.get("665450f1c84bb1e76f9d760e"),
            row.get("661fbe9677546c70a2be388a")
            ]
            rows.append(metrow)
        return rows

def save_sql(data):
    conn=pymysql.connect(
        host='192.168.6.115',
        user='admin',
        password='pisen1',
        database='Pisen_DW',
        port=9030
    )
    with conn.cursor() as cursor:
        sql=('''
            insert into ODS_SG_STORE_TEST(stor,stornumber,storname,custnumber,sotr_add,longitude,latitude,
             storstatus,opentime)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''')
        cursor.executemany(sql,data)
        conn.commit()

# 调用函数时传递不同的 page_size 值
page_size = 100
page_index = 1
allrows=[]
while True:
    rows=fetch_data(page_size, page_index)
    if rows:
        allrows.extend(rows)
        page_index+=1
    else:
        break
#print(allrows)
save_sql(allrows)