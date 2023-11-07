import requests,sys,bs4,webbrowser
#获取命令行参数
res=requests.get('https://www.google.com.hk/search?q=11') #+' '.join(sys.argv[1:]))
res.raise_for_status()
#取得查询结果页面
soup=bs4.BeautifulSoup(res.text)
Aelemt=soup.select('div>a')
print(len(Aelemt))
#为前几个结果打开新页签

minurl=min(5,len(Aelemt))
for i in range(minurl):
    webbrowser.open(Aelemt[i].get('href'))
