import requests,json,re
import jieba

url="https://s.weibo.com/weibo?q=%23%E7%BA%A2%E6%96%91%E7%8B%BC%E7%96%AE%E4%BD%A0%E4%BA%86%E8%A7%A3%E5%A4%9A%E5%B0%91%23&typeall=1&suball=1&timescope=custom%3A2023-12-13-9%3A2023-12-13-12&Refer=g"
heard={
    "Referer": "https://s.weibo.com/weibo?q=%23%E7%BA%A2%E6%96%91%E7%8B%BC%E7%96%AE%E4%BD%A0%E4%BA%86%E8%A7%A3%E5%A4%9A%E5%B0%91%23",
    "Cookie": "_s_tentry=www.google.com; UOR=www.google.com,open.weibo.com,www.google.com; Apache=3687255896763.0874.1702434328914; SINAGLOBAL=3687255896763.0874.1702434328914; ULV=1702434328941:1:1:1:3687255896763.0874.1702434328914:; SUB=_2A25IfWheDeRhGeNH6VUU9ifKyT6IHXVr8-WWrDV8PUNbmtB-LVfFkW9NStqHf1zZuqNmCG2lKu79ZzoPwpgCWtqT; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWv4dBrY3opCnHlFPAIhWlW5JpX5o275NHD95Qf1KzNSKq4SozEWs4DqcjAi--4iK.fi-isi--Xi-zRiKy2i--fi-2Xi-2Ni--NiKLWiKnXi--ciKLsi-8si--fiKy2iK.Neo5pS7tt; ALF=1703039631; SSOLoginState=1702434830",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin"
}
text1=requests.get(url,headers=heard)
comment_id=re.findall('(?<=mid=")\d{16}',text1.text)
print(comment_id)

def get_content(comment_id):
    article_url='https://m.weibo.cn/detail/' + comment_id
    html_text=requests.get(article_url).text
    find_title = re.findall('.*?"text": "(.*?)",.*?', html_text)[0]
    title_text = re.sub('<(S*?)[^>]*>.*?|<.*? />', '', find_title) 
    return title_text

def list_artical(comment_id):
    with open('article.txt','w',encoding='utf-8') as f:
        for c in range(len(comment_id)):
            get_content(comment_id[c])
           # print(get_content(comment_id[c]))
            f.write(get_content(comment_id[c])+'\n')


if __name__ == '__main__':
    print(list_artical(comment_id))  # 全模式
