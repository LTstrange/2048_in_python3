import random

field=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def add_number():#随机选择添加数字
    number_type = random.randint(0,3)
    if number_type == 0:
        add_num = 4
    else:
        add_num = 2
    return add_num

def add_add(obj,x_max=3,y_max=3):#添加数字
    zero_location =[]
    for y_ind,y_obj in enumerate(obj):
        for x_ind,x_obj in enumerate(y_obj):
            if x_obj == 0:
                zero_location.extend([[x_ind,y_ind]])
    location_ind=random.randint(0,len(zero_location)-1)
    obj[zero_location[location_ind][0]][zero_location[location_ind][1]] = add_number()
    return obj

def print_screen():#打印屏幕
    global field
    global score
    print('--------------------')
    print('your score is:',score)
    print(field[0])
    print(field[1])
    print(field[2])
    print(field[3])

def operate():
    operate = input('whats your operate:')
    return operate

def leftward(obj):
    for ind,y_obj in enumerate(obj):
        if y_obj[0] == y_obj[1]:
            obj[ind][0] = y_obj[0] + y_obj[1]
            if y_obj[2] == y_obj[3]:
                obj[ind][1] = y_obj[2] +y_obj[3]
                obj[ind][2] = 0
                obj[ind][3] = 0
            else:
                obj[ind][1] = obj[ind][2]
                obj[ind][2] = obj[ind][3]
                obj[ind][3] = 0
        elif y_obj[0] == 0:
            if
    return obj
                

score = 0


field = add_add(field)
field = add_add(field)
print_screen()
operate()
field = leftward(field)
print_screen()