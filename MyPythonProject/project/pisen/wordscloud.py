import pymysql
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
data_list=[]
conn=pymysql.connect(
    host='192.168.6.115',
    port=9030,
    user='admin',
    password='pisen1',
    database='Pisen_DW'
)

cursor=conn.cursor()
cursor.execute("select upper(a.product_name) from DWD_SG_SALE a")
for row in cursor.fetchall():
    data_list.append(row[0])
cursor.close()
conn.close()
print(len(data_list))
# jieba.re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\-._]+)", re.U)
stopwords_path = "stopwords.txt"
stopwords = set()
with open(stopwords_path, "r", encoding="utf-8") as f:
    for line in f:
        stopwords.add(line.strip())
jieba.load_userdict("custom_dict.txt")
text=" ".join(data_list)
word_list = jieba.lcut(text)
# print(word_list)
word_list = [word for word in word_list if word not in stopwords]

words = ",".join(word_list)
# print(words)
wc = WordCloud(font_path="msyh.ttc", max_font_size=450,width=1920, height=1080, mode="RGBA",background_color=None,collocations=False)
wc.generate(words)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()