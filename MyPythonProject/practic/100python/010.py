from turtle import *
#初始化参数
win=False
speed(0)
bgcolor("lightgreen")
yanse="black"

gz=40
##画棋盘
judge = Turtle()
judge.up()
judge.goto(-460, 330)
judge.write("谁下", font=("Kai", 40, "bold"))
judge.color(yanse)
judge.goto(-420, 300)
judge.dot(30)

# 画19条横线
for i in range(19):
    up()
    goto(-gz*9, gz*(9-i))
    down()
    fd(gz*18)
    bk(gz*18)

rt(90)
# 画19条竖线
for i in range(19):
    up()
    goto(-gz*(9-i), gz*9)
    down()
    fd(gz*18)
    bk(gz*18)

# 画最外面的粗边框
pensize(5)
for i in range(4):
    fd(gz*18)
    rt(90)
##进行判断逻辑
m =[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def check(i,j):
    global win
    g=[0]*8
    fw = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    for index in range(8):
        d=fw[index]
        next_i=i+d[0]
        next_j=j+d[1]
        while next_i in range(19) and next_j in range(19) and m[next_i][next_j]==m[i][j]:
            g[index]+=1
            next_i+=d[0]
            next_j+=d[1]
    for index in range(4):
        if g[index]+g[index+4]+1>=5:
            win=True
            goto(0,0)
            if yanse=='black':
                write('black win',font=('Arial',100,''),align='center')
            else:
                write('white win',font=('Arial',100,''),align='center')
            break

##鼠标进行游戏并调用判断
def play(x,y):
    if not win:
        global yanse
        global gz
        color(yanse)
        up()
        x = round(x/gz)*gz
        y = round(y/gz)*gz
        i = int(9 - y / gz)
        j = int(x / gz + 9)
        if i >= 0 and i <= 18 and j >=0 and j<=18:
            if m[i][j] == 0:
                goto(x, y) 
                dot(30)
                
                if yanse == "black":
                    m[i][j] = 1
                    check(i, j)
                    yanse="white"
                else:
                    m[i][j] = 2
                    check(i, j)
                    yanse="black"
                    
                judge.color(yanse)
                judge.dot(30)
                
onscreenclick(play, 1)
done()