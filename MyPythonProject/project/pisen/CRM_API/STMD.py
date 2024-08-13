#目的:使用接口自动对接crm实体门店信息，只获取最近更新日期一月之内的数据
#1.从接口获取相关数据（字段信息）
#2.写入数据库具体表中（文本文件中）

import requests,pymysql
import json,csv
from datetime import datetime,timedelta

def fetch_data(page_size, page_index):
    url = "https://mingdao.yunma99.com/api/v2/open/worksheet/getFilterRows"
    from_day=datetime.now()-timedelta(days=1)
    yestoday=from_day.strftime('%Y-%m-%d')

    payload = json.dumps({
        "appKey": "9eb44cd3fc1e56b5",
        "sign": "NmMwNGQ3NDA0ODQ4OTkyYjk4YTNlYmUzZWNjNzU4MmU3NGVhMTNhZGU0ZmMzOGE0YTYyOWU3Mjc0MWYyM2Y0NA==",
        "worksheetId": "stmd",
        "viewId": "",
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
            json_field=row.get("65bc587fae0428df507eee68")
            try:
                json_office=json.loads(json_field)[0].get("name",None)
            except IndexError as e:
                json_office=None

            metrow=[
            row.get("65b89949b5486cd1068ca6ea"),
            row.get("65a10723a256f71f993ca4b6"),
            row.get("659df741a256f71f993c9b6f"),
            row.get("659df741a256f71f993c9b71"),
            row.get("659df741a256f71f993c9b73"),
            row.get("659df741a256f71f993c9b74"),
            row.get("65a1078ca256f71f993ca4de"),
            row.get("65e973bfae0428df507f14ac"),
            json_office,
            row.get("660bd0f9896e647b38f4c07b"),
            row.get("660bd0f9896e647b38f4c07c"),
            row.get("660bd0f9896e647b38f4c07d"),
            row.get("659f4bc8a256f71f993ca069")
            ]
            rows.append(metrow)
        return rows

def save_csv(data):
    headers=['custnumber','custname','shopsign']    
    csv_file='/data/app/dolphinscheduler/ui/STMD.csv'

    with open(csv_file,mode='w',newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print('data success written in file!!!')

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
            insert into ODS_SG_CUSTOM_TEST(custnumber,custname,shopsign,shop_add,longitude,latitude,shoptype,
             shopnature,office,province,city,area,developtime)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
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
save_sql(allrows)