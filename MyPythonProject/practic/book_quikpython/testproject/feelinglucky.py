#从命令行获取关键字 
#打开浏览器并运行查询结果
#利用html标记 获取url
#打开web浏览器
import bs4,webbrowser,sys,requests
a=' '.join(sys.argv[1:])
res=requests.get('http://google.com/search?q='+a)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)
elem=soup.select('.r a')
numopen=min[5,len[elem]]
for i in range(numopen):
    webbrowser.open(elem[i].get('href'))


