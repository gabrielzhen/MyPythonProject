#下载漫画网站xkcd的漫画
import requests,sys,bs4,os
url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
for i in range(10):
    print('downloading')
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)
    elem=soup.select('#comic img')
    if elem==[]:
        print('can not found')
    else:
        elemurl='http:'+elem[0].get('src')
        res=requests.get(elemurl)
        imagefile=open(os.path.join('xkcd',os.path.basename(elemurl)),'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()
    prevlink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevlink.get('href')
    i+=i
    
