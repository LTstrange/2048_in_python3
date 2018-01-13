import random
def Fup(screen):#这个函数将每个竖列向上加成并补零
    for i,s in enumerate(screen):
        if i < 4:
            if screen[i] == screen[i+4]:
                screen[i] = screen[i] + screen[i+4]
                screen[i+4] = screen[i+8]
                screen[i+8] = screen[i+12]
                screen[i+12] = 0
        elif i < 8:
             if screen[i] == screen[i+4]:
                screen[i] = screen[i] + screen[i+4]
                screen[i+4] = screen[i+8]
                screen[i+8] = 0
        elif i < 12:
            if screen[i] == screen[i+4]:
                screen[i] = screen[i] + screen[i+4]
                screen[i+4] = 0
    return screen


def Fu2r(screen):#这个函数将4*4的表格沿一条过原点、第二象限、第四象限的四十五度的线翻转
    mix = list( zip( list( zip(screen[0:4],screen[8:12]) ),list(zip(screen[4:8],screen[12:16])) ) )
    temp = []
    for each in mix:
        temp.extend(list(each))
    screen = []
    for each in temp:
        screen.extend(list(each))
    return screen


def randnum():#这个函数生成了2或者4，比率是1:4
    temp = random.randint(0,5)
    if temp == 0:
        randnum =4
    else:
        randnum = 2
    return randnum


screen = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while True:
    print ("——————2048——————")
    rand = random. randint(0,screen.count(0))#这里定义了一个数字rand，用来确定随机数位置
    temp = 0
    for zero in screen:
        if zero == 0:
            if temp == rand:
                screen[temp] = randnum()
        temp += 1
    

    print('\t',screen[0:4],'\n\t',screen[4:8],'\n\t',screen[8:12],'\n\t',screen[12:16])#这里输出了屏幕
    
    ope = str(input("你的操作是(wasd)："))


    
    #以下决定了那些操作进行哪些运算
    if ope == 'w':
        screen = Fup(screen)
    elif ope == 'a':
        screen = list(reversed(screen))
        screen = Fup(screen)
        screen = list(reversed(screen))
    else:
        screen = Fu2r(screen)
        if ope == 's':
            screen = Fup(screen)
        if ope == 'd':
            screen = list(reversed(screen))
            screen = Fup(screen)
            screen = list(reversed(screen))
        screen = Fu2r(screen)
