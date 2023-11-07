import requests,os,bs4
url='https://xkcd.com/'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
#todo:下载网页
    res=requests.get(url)
    res.raise_for_status()
#todo:找到图片url
    soup=bs4.BeautifulSoup(res.text)
    elem=soup.select('#comic img')
    if elem==[]:
        print('can not find the picture')
    else:
        comicurl='https:'+elem[0].get('src')
        res=requests.get(comicurl)
        res.raise_for_status()
#todo:下载图像，并保存
        migfile=open(os.path.join('xkcd',os.path.basename(comicurl)),'wb')
        for chunk in res.iter_content(1000):
            migfile.write(chunk)
        migfile.close()
#todo:找到下一个链接url，重复上面步骤
    prelink=soup.select('a[rel="prev"]')
    url='https://xkcd.com'+prelink[0].get('href')
