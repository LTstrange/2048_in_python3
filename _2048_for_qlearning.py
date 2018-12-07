#!/user/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LTstrange'

import random
import copy


def in_ope():
    while True:
        ope = input("你的操作是：\n（wasd）\n使用“exit()”来退出\n")
        if ope == 'w':
            return 0
        if ope == 'd':
            return 1
        if ope == 's':
            return 2
        if ope == 'a':
            return 3
        if ope == 'exit()':
            exit()
        else:
            print('please input w,s,a,d\nmeans up,down,left,right')
            continue


class GAME:
    def __init__(self):
        self.field = [[0 for i in range(4)] for x in range(4)]
        self.field_ = self.field
        self.actions = [0, 1, 2, 3]
        self.score = 0
        self.reward = 0
        self.done = False

    def restart(self):
        self.field = [[0 for i in range(4)] for x in range(4)]
        self.score = 0
        self.done = False
        self.add_number()
        self.add_number()

    def render(self):  # 打印屏幕(finished
        print('--------------------')
        print('your reward is:', self.reward)
        print('\t%d\t%d\t%d\t%d\n' % (self.field[0][0], self.field[0][1], self.field[0][2], self.field[0][3]))
        print('\t%d\t%d\t%d\t%d\n' % (self.field[1][0], self.field[1][1], self.field[1][2], self.field[1][3]))
        print('\t%d\t%d\t%d\t%d\n' % (self.field[2][0], self.field[2][1], self.field[2][2], self.field[2][3]))
        print('\t%d\t%d\t%d\t%d\n' % (self.field[3][0], self.field[3][1], self.field[3][2], self.field[3][3]))

    def step(self, ope):
        score_ = self.score
        field_ = []
        field_ = copy.deepcopy(self.field)
        self.move(ope)
        if field_ != self.field:
            self.add_number()
        self.reward = self.score - score_
        if self.check():
            return self.field, self.reward, False
        else:
            return self.field, self.reward, True

    def add_number(self):  # 随机选择添加数字(finished
        add_num = 2 if random.randrange(0, 10) > 1 else 4
        for i in self.field:
            for x in i:
                if x == 0:
                    flag = 1
        if flag:
            l = []
            for ind_y, y in enumerate(self.field):
                for ind_x, x in enumerate(y):
                    if x == 0:
                        l.append([ind_y, ind_x])
            if len(l) > 0:
                position = l[random.randint(0, len(l) - 1)]
                self.field[position[0]][position[1]] = add_num

    def check(self):  # 前一个代表游戏是否结束，后一个代表是否还有空位
        for i in range(4):
            for j in range(3):
                if self.field[i][j] == 0 or self.field[i][j] == self.field[i][j+1] or self.field[j][i] == self.field[j+1][i]:
                    return True
                else:
                    return False

    def move(self, ope):  # 3=l 0=u 1=r 2=d
        if ope == 3:
            self.leftward()
        elif ope == 0:
            self.Fl2u()
            self.leftward()
            self.Fl2u()
        elif ope == 1:
            self.Fl2r()
            self.leftward()
            self.Fl2r()
        elif ope == 2:
            self.Fl2u()
            self.Fl2r()
            self.leftward()
            self.Fl2r()
            self.Fl2u()

    def leftward(self):  # 使field向左滑动(finished
        for ind, y_obj in enumerate(self.field):
            num_zero = y_obj.count(0)
            for i in range(0, num_zero):
                self.field[ind].remove(0)
                self.field[ind].append(0)
            if y_obj[0] == y_obj[1]:
                self.field[ind][0] = y_obj[0] + y_obj[1]
                self.score += self.field[ind][0]
                self.field[ind][1] = self.field[ind][2]
                self.field[ind][2] = self.field[ind][3]
                self.field[ind][3] = 0
            if y_obj[1] == y_obj[2]:
                self.field[ind][1] = y_obj[1] + y_obj[2]
                self.score += self.field[ind][1]
                self.field[ind][2] = self.field[ind][3]
                self.field[ind][3] = 0
            if y_obj[2] == y_obj[3]:
                self.field[ind][2] = y_obj[2] + y_obj[3]
                self.score += self.field[ind][2]
                self.field[ind][3] = 0

    def Fl2u(self):  # 转换field方向（左到上）(finished
        temp = list(zip(self.field[0], self.field[1], self.field[2], self.field[3]))
        self.field = []
        for each in temp:
            self.field.extend([list(each)])

    def Fl2r(self):  # 转换field方向（左到右）(finished
        for ind, y_obj in enumerate(self.field):
            y_obj.reverse()
            self.field[ind] = y_obj


if __name__ == '__main__':
    env = GAME()
    env.restart()
    while True:
        env.render()
        env.step(in_ope())
