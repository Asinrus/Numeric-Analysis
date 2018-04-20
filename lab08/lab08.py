import sys
import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log

def f(x):
    return atan(x)

def recurs_f(X):
    if (len(X) > 2):
        return (1/(X[0] - X[-1])) * ( recurs_f(X[:-1]) - recurs_f(X[1:]) )
    elif (len(X) == 2):
        return (1/(X[0] - X[-1])) * ( f(X[0]) - f(X[1]) )
    else:
        return f(X[0])

def recurs_f_string(X,i):
    s ='f('
    for j in range(i):
        s += 'x%d'%(j) + ','
    s = s[:-1] + ')'
    return s

def que_f(X,i,x):
    s = 1
    for j in range(i):
        s *= (x-X[j])
    return s

def w_i(X,i):
    s=1
    for j in range(len(X)):
        if j != i:
            s *= X[i] - X[j]
    try: 
        return 1/s
    except ZeroDivisionError:
        return 1

def string(X,i):
    s = ''
    for j in range(len(X)):
        if j != i:
            s += '(x -'+str(X[j])+')'
    return s

def lan(X, x=False):
    coef = np.array([f(i) for i in X ])
    if x:
        s = 0
        for i in range(len(X)):
            s += coef[i]  * w_i(X,i) * np.prod([x - X[j] for j in range(len(X)) if j!=i]) 
        return s
    else:
        s = ''
        for i in range(len(X)):
            s +=   str(coef[i] * w_i(X,i)) + string(X,i) +'+'
        return s[:-1]

def new(X,x=False):
    
    if x:
        s = 0 
        for i in range(len(X)):
            s += que_f(X,i,x)*recurs_f(X[:i+1])
        return s
    else:
        s= ''
        for i in range(len(X)):
            s += str(que_f(X,i,x))+recurs_f_string(X,i+1)+'+'
        return s[:-1]

if __name__ == '__main__':
    X = -0.5
    X_lan = [-3,-1,1,3]
    X_new = [-3, 0, 1, 3]
    print('Ряд Лангранжа :\n', lan(X_lan))
    print('Значение ряда Лангранжа в точке {}  = {}'.format(X,lan(X_lan,X)))
    print("Неточность  = {}".format(abs(lan(X_lan,X)-f(X))))
    print('Ряд Ньютона :\n', new(X_new))
    print('Значение ряда Ньютона в точке {}  = {}'.format(X,new(X_new,X) ) )
    print("Неточность  = {}".format(abs(new(X_new,X)-f(X))))