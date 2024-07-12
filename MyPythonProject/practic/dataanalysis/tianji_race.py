#田忌赛马 用计算机计算所有组合的可能性
tian={'q1':1.5,'q2':2.5,'q3':3.5}
qi={'q1':1,'q2':2,'q3':3}
tian2=['q1','q2','q3']
#递归
results=[]
def race_list(lists):
    if len(lists)==1:
        return lists
    elif len(lists)==2:
        return [[lists[0],lists[1]],[lists[1],lists[0]]]
    else:
        for i in lists:
            sub_list=lists.copy()
            sub_list.remove(i)
            tmp_result=race_list(sub_list)
            for t in tmp_result:
                results.append([i]+t)
        return results

print(race_list(tian2))