# -*- coding: utf-8 -*-
# 杨辉三角
def triangle(n):
    L=[1]
    while True:
        yield(L)
# 末尾加0
        L.append(0)
# L[-1]刚好也为0
        L=[L[i]+L[i-1] for i in range(len(L))]
        if len(L)>n:
            break
    return "done"

g=triangle(10)
for i in g:
    print(i)

