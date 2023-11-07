import requests,os,bs4,threading
os.makedirs('xkcd',exist_ok=True)

def downloadxkcd(startcomic,endcomic):
    for urlNumber in range(startcomic,endcomic):
        print('Downloading page http://xkdc.com/%s...'%(urlNumber))
        res=requests.get('http://xkcd.com/%s'%(urlNumber))
        res.raise_for_status()

        soup=bs4.BeautifulSoup(res.text)
        comicElem=soup.select('#comic img')
        if comicElem==[]:
            print('could not find the image')
        else:
            comurl=comicElem[0].get('src')
            print('Downloading image %s..'%(comurl))
            res=requests.get(comurl)
            res.raise_for_status()

            imageFile=open(os.path.join('xkcd',os.path.basename(comurl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

downloadThreads=[]
for i in range(0,500,50):
    downloadThread=threading.Thread(target=downloadxkcd,args=[i,i+49])
    downloadThreads.append(downloadThread)
    downloadThread.start()

for thread in downloadThreads:
    thread.join()
print('Done')
