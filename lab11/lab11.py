# -*- encoding: utf-8 -*-
import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log
import matplotlib.pyplot as plt
'''Численное дифференцирование. Исправить и получить через многочлен 5-ой степени'''



def recurs_f(X,y):
    if (len(X) > 2):
        return (1/(X[0] - X[-1])) * ( recurs_f(X[:-1],y[:-1]) - recurs_f(X[1:],y[1:]) )
    elif (len(X) == 2):
        return (1/(X[0] - X[-1])) * ( y[0] - y[-1])
    else:
        return y[0]


def que_f(X,i,x):
    s = 0
    for j in range(i):
        der = 1
        for k in range(i):
            if k !=j: 
                der *= x - X[k]
        s += der
    return s

def que_df(X,i,x):
    s = 0
    der = 0
    for j in range(i):
        for k in range(i):
            if k !=j:
                der = 1
                for t in range(i):
                    if t!=k and t!=j:
                       der *= x - X[t]  
                s += der
    return s


def der(X,y,x):
    s = 0 
    for i in range(1,len(X)):
        s += que_f(X,i,x)*recurs_f(X[:i+1],y[:i+1])
    return s
    
def dder(X,y,x):
    s = 0 
    for i in range(2,len(X)):
        if i ==2:
            s += 2*recurs_f(X[:i+1],y[:i+1])
        else:
            s += que_df(X,i,x)*recurs_f(X[:i+1],y[:i+1])
    return s    

if __name__ == '__main__':
    X_0 = 1.
    X = [0,.5,1.,1.5,2.]
    y = [0,.97943,1.8415,2.4975,2.9093]

    print('Derivative in point {} = {}'.format(X_0,der(X,y,X_0) ) )
    print('Second derivative in point {} = {}'.format(X_0,dder(X,y,X_0) ) )