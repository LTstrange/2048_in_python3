import random

def version():
    print('version:1.0.0')

field=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
score = 0

def restart():#重置游戏(finished
    global field
    field=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    field = add_add(field)
    field = add_add(field)

def add_number():#随机选择添加数字(finished
    number_type = random.randint(0,3)
    if number_type == 0:
        add_num = 4
    else:
        add_num = 2
    return add_num

def add_add(obj,x_max=3,y_max=3):#添加数字(finished
    zero_location =[]
    for y_ind,y_obj in enumerate(obj):
        for x_ind,x_obj in enumerate(y_obj):
            if x_obj == 0:
                zero_location.extend([[x_ind,y_ind]])
    location_ind=random.randint(0,len(zero_location)-1)
    obj[zero_location[location_ind][0]][zero_location[location_ind][1]] = add_number()
    return obj

def print_screen():#打印屏幕(finished
    global field
    global score
    print('--------------------')
    print('your score is:',score)
    print(field[0][0],field[0][1],field[0][2],field[0][3])
    print(field[1][0],field[1][1],field[1][2],field[1][3])
    print(field[2][0],field[2][1],field[2][2],field[2][3])
    print(field[3][0],field[3][1],field[3][2],field[3][3])

def operates():#决定输入操作(finished
    operate = input('whats your operate:')
    return operate

def leftward(obj):#使field向左滑动(finished
    global score
    for ind,y_obj in enumerate(obj):
        num_zero = y_obj.count(0)
        for i in range(0,num_zero):
            obj[ind].remove(0)
            obj[ind].append(0)
        if y_obj[0] == y_obj[1]:
            obj[ind][0] = y_obj[0] + y_obj[1]
            score += obj[ind][0]
            obj[ind][1] = obj[ind][2]
            obj[ind][2] = obj[ind][3]
            obj[ind][3] = 0
            if y_obj[1] == y_obj[2]:
                obj[ind][1] = y_obj[1] +y_obj[2]
                score += obj[ind][1]
                obj[ind][2] = obj[ind][3]
                obj[ind][3] = 0
        elif y_obj[1] == y_obj[2]:
            obj[ind][1] = y_obj[1] + y_obj[2]
            score += obj[ind][1]
            obj[ind][2] = y_obj[3]
            obj[ind][3] = 0
        elif y_obj[2] == y_obj[3]:
            obj[ind][2] = y_obj[2] + y_obj[3]
            score += obj[ind][2]
            obj[ind][3] = 0
    return obj

def Fl2r(obj):#转换field方向（左到右）(finished
    for ind,y_obj in enumerate(obj):
        y_obj.reverse()
        obj[ind] = y_obj
    return obj

def Fl2u(obj):#转换field方向（左到上）(finished
    temp = list(zip(obj[0],obj[1],obj[2],obj[3]))
    obj = []
    for each in temp:
        obj.extend([list(each)])
    return obj
        
def final_operate():#翻译操作符为具体操作函数(finished
    global field
    while True:
        operate = operates()
        if operate == 'l':
            field = leftward(field)
            break
        elif operate == 'u':
            field = Fl2u(field)
            field = leftward(field)
            field = Fl2u(field)
            break
        elif operate == 'r':
            field = Fl2r(field)
            field = leftward(field)
            field = Fl2r(field)
            break
        elif operate == 'd':
            field = Fl2u(field)
            field = Fl2r(field)
            field = leftward(field)
            field = Fl2r(field)
            field = Fl2u(field)
            break
        else:
            print('please input u,d,l,r\nmeans up,down,left,right')
            continue

def __main__():
    global field
    restart()
    print_screen()
    while True:
        final_operate()
        field = add_add(field)
        print_screen()
        zero_number = 0
        for each in field:
            zero_number += field.count(0)
        if zero_number != 0:
            print('game over')
            ope = input('do you want play again?')
            if ope == 'y':
                restart()
                print_screen()
                continue
            else:
                break

__main__()