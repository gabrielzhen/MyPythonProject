#世界杯32强比赛 使用组合
cups=[1,2,3]
rankd=[]

def comb(lists,m):
    if len(rankd)==m:
        return rankd
    elif m==1:
        return lists
    else:
        for i in lists:
            sublists=lists[1:]
            tmplists=comb(sublists,m-1)
            for k in tmplists:
                rankd.append([i]+comb(sublists,m-1))
        return rankd
        
print(comb(cups,2))
