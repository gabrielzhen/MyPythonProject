#通过xhr进行分析，豆瓣的xhr需要改造headers，这是一种还有一种是直接html生成好进行解析，这里面又有两种，一种是静态的页面直接翻页循环抓取，
# 另一种是需要调用driver等待页面完全生成之后，再进行xpath解析
import requests,json
url='https://m.douban.com/rexxar/api/v2/search?q=王祖贤&type=&loc_id=&start=11&count=10&sort=relevance'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Referer':'https://www.douban.com/search?q=%E7%8E%8B%E7%A5%96%E8%B4%A4'
}
res=requests.get(url,headers=headers)
jsons=json.loads(res.content)
pics=jsons['contents']['items'][2]['target']['photos'][1]['normal']['url']
print(pics)