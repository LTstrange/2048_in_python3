#!/user/bin/env python
# coding=utf-8
import random
import copy

def version():
    print('version:1.1.0')

def restart():#重置游戏(finished
    score = 0
    field= [[0 for i in range(4)] for j in range(4)]
    field = add_add(field)
    field = add_add(field)
    return field,score

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

def print_screen(field,score):#打印屏幕(finished
    print('--------------------')
    print('your score is:',score)
    print('%d\t%d\t%d\t%d'%(field[0][0],field[0][1],field[0][2],field[0][3]))
    print('%d\t%d\t%d\t%d'%(field[1][0],field[1][1],field[1][2],field[1][3]))
    print('%d\t%d\t%d\t%d'%(field[2][0],field[2][1],field[2][2],field[2][3]))
    print('%d\t%d\t%d\t%d'%(field[3][0],field[3][1],field[3][2],field[3][3]))

def operates():#决定输入操作(finished
    operate = input('whats your operate:')
    return operate

def leftward(obj,score):#使field向左滑动(finished
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
        if y_obj[2] == y_obj[3]:
            obj[ind][2] = y_obj[2] + y_obj[3]
            score += obj[ind][2]
            obj[ind][3] = 0
    return obj,score

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
        
def final_operate(field,score):#翻译操作符为具体操作函数(finished
    while True:
        operate = operates()
        if operate == 'a':
            field,score = leftward(field,score)
            break
        elif operate == 'w':
            field = Fl2u(field)
            field,score = leftward(field,score)
            field = Fl2u(field)
            break
        elif operate == 'd':
            field = Fl2r(field)
            field,score = leftward(field,score)
            field = Fl2r(field)
            break
        elif operate == 's':
            field = Fl2u(field)
            field = Fl2r(field)
            field,score = leftward(field,score)
            field = Fl2r(field)
            field = Fl2u(field)
            break
        else:
            print('please input w,s,a,d\nmeans up,down,left,right')
            continue
    return field,score

def cheak(field):
    for i in range(4):
        for i in range(4):
            if i<3 and field[i][j] == field[i+1][j]:
                return False
        for j in range(4):
            if j<3 and field[i][j] == field[i][j+1]:
                return False

def main(key=0):
    field,score = restart()
    print_screen(field,score)
    while True:
        tmp = copy.deepcopy(field)
        field,score = final_operate(field,score)
        if tmp != field:
            field = add_add(field)
            print_screen(field,score)
            zero_number = 0
        else:
            print('This move has no efficient')
        for each in field:
            zero_number = field.count(0)
        if zero_number != 0:
            print('game over')
            ope = input('do you want play again?')
            if ope == 'y':
                field,score = restart()
                print_screen(field,score)
                continue
            else:
                break

if __name__ == '__main__':
    main()