#!/usr/bin/env python
# -*- coding: utf-8 -*-
def triangle(n):
    L=[1]
    while True:
        yield(L)
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]
        if len(L)>n:
            break
    return 

g=triangle(10)
for i in g:
    print(i)

