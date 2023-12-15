import requests,re,json

#登录验证
url='https://metshop.vip/users/login/vcode'
data1={"referrerUserNo":None,"vcode":"lkasjd12308ASD123as..","targetAddr":"18688888230","targetType":"SMS","terminalName":"mobile"}
response=requests.post(url,json=data1)
print(response.text)

#获取页面信息


#遍历文件进行登录，成功的进行下一步获取页面信息，并进行统计