#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Horner多项式求值算法
"""
    Topic: sample
    Desc : Horner多项式求值算法
        P(x) = Σ(k=0,n)a(k)x^k = a0 + x(a1 + x(a2+ ... + x(an-1 + x*an)...))
"""
__author__ = 'Xiong Neng'


def hornerPoly(coefficientArr, x):
    res = 0
    for i in range(len(coefficientArr))[-1::-1]:
        res = coefficientArr[i] + x * res
    return res

if __name__ == '__main__':
    print(hornerPoly((1, 2, 3), 2))
