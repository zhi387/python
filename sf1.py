# -*- coding: utf-8 -*-
# 汉诺塔a 移到c
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)
move(3,'A','B','C')
