import vincent

most_common=[('day', 476), ('game', 160), ('ireland', 143), ('england', 132), ('great', 105), ('today', 104), ('best', 97), ('well', 90), ('ever', 89), ('incredible', 87), ('amazing', 84), ('done', 82), ('amp', 71), ('games', 66), ('points', 64), ('monumental', 58), ('strap', 56), ('world', 55), ('team', 55), ('http://t.co/bhmeorr19i', 53)]
labels, freq = zip(*most_common)
# bar = vincent.Bar(dict(data=freq, x=labels))

# # 设置图表标题和标签
# bar.axis_titles(x='词汇', y='频率')
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')

# 保存图表为JSON文件
bar.to_json('term_freq.json')
