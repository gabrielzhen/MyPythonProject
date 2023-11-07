tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(datas):
    widths=[0]*len(datas)
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            if widths[i]<len(datas[i][j]):
                widths[i]=len(datas[i][j])
    
    for a in range(len(widths)):

    return widths

print(printTable(tableData))
