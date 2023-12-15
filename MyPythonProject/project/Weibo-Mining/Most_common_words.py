import jieba,re,json
from collections import Counter
# 利用正则表达式对象进行分词
regex_str=[
    r'#(.*?)#',
    r'^@.*[\n\s:]'
]
token_re=re.compile(r'('+'|'.join(regex_str)+')',re.UNICODE)
jsonlist=[]
def tokenize(s):
    # print(token_re.findall(s))
    return token_re.findall(s)
# 读取文件并且进行分词计数
def jsonlists():
    with open('article.txt','r',encoding='utf-8') as f:
        count_all=Counter()
        for line in f.readlines():
            tag=[term[1] for term in tokenize(line)]
            # print(tag)
            count_all.update(tag)
    # print(count_all.most_common(10))
    # 保存为json格式的字符串
    for word,count in count_all.most_common(10):
        temp={'word':word,'count':count}
        jsonlist.append(temp)
    print(json.dumps(jsonlist,ensure_ascii=False))
    with open('most_common.json','w',encoding='utf-8') as f:
        f.write(json.dumps(jsonlist,ensure_ascii=False))
if __name__ == '__main__':
    jsonlists()