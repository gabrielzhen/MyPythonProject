import requests
url='https://fanyi.baidu.com/sug'

while True:
    text=input('请输入中文或者英语').strip()
    if text=='q':
        break

    data={'kw':text}
    resp=requests.post(url,data)
    
    if resp.json()['errno']==0:
        for i in resp.json()['data']:
            if i['k']==text:
                print(i['v'])
                break
            else:
                print('没有找到')
    else:
        print('错误') 
    