#Решение краевых задач для нелинейных дифференциальных уравнений методом конечных разностей.

import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log,tan,e
import matplotlib.pyplot as plt

def f(x):
    return x**3 / 3

def RRR(A,X_old,f,h,eps,p):
    X_0 = 0.
    X_k = 1.
    h_1 = 2*h
    X = np.arange(X_0,X_k+h_1, h_1)
    dA = f(X,h_1,eps)
    E = []
    for i in range(len(X)):
        if X[i] in X_old:
            j = list(X_old).index(X[i])
            error = abs(dA[i] - A[j]) / (2**p-1)
            E.append(error)
    return E

def konechno(X,h,eps = 0.001,dr = False):
    n = X.shape[0]
    y = [1/3 * i for i in X]
    A = np.zeros((n-2,n-2),dtype = float)
    B = np.zeros(n-2,dtype = float)
    answer = []
    B[0] = 2*X[0]* (1 + X[0]**3 /3)
    A[0][0] = -2/(h*h) + 2*X[0] * (1 + 0.5*X[0]) 
    A[0][1] =  1/(h*h) + 0.5*y[0]/h
    for i in range(1,n-3):
        A[i][i-1] = 1/(h*h) + 0.5*y[i]/h 
        A[i][i] = -2/(h*h) + 2*X[i] * (1 + 0.5*X[i])
        A[i][i+1] = 1/(h*h) + 0.5 * y[i]/h
        B[i] = 2* X[i] *(1 + X[i]/ 3)
    A[-1][-2] = 1/(h*h) + 0.5*y[-2]/h 
    A[-1][-1] = -2/(h*h) + 2*X[-2]*(1+0.5*X[-2])
    B[-1] = 2* X[-2] *(1 + X[-2]/ 3) - 1/3 * (1/(h*h) + y[-2]/ 2 /h)
    C = np.linalg.solve(A, B)
    y_new = [i for i in C]
    y_new.insert(0,0)
    y_new.append(1/3)
    k = 1

    while True and k < 100:
        y_old = [i for i in y_new]

        A = np.zeros((n-2,n-2),dtype = float)
        B = np.zeros(n-2,dtype = float)
        B[0] = 2*X[0]* (1 + X[0]**3 /3)
        A[0][0] = -2/(h*h) + 2*X[0] * (1 + 0.5*X[0]) 
        A[0][1] =  1/(h*h) + 0.5*y_old[0]/h
        for i in range(1,n-3):
            A[i][i-1] = 1/(h*h) + 0.5*y_old[i]/h 
            A[i][i] = -2/(h*h) + 2*X[i] * (1 + 0.5*X[i])
            A[i][i+1] = 1/(h*h) + 0.5 * y_old[i]/h
            B[i] = 2* X[i] *(1 + X[i]/ 3)
        A[-1][-2] = 1/(h*h) + 0.5*y_old[-2]/h 
        A[-1][-1] = -2/(h*h) + 2*X[-2]*(1+0.5*X[-2])
        B[-1] = 2* X[-2] *(1 + X[-2]/ 3) - 1/3 * (1/(h*h) + y_old[-2] / 2 /h)
        C = np.linalg.solve(A, B)
        
        y_new = [i for i in C]
        y_new.insert(0,0)
        y_new.append(1/3)

        e = [(y_old[i] - y_new[i])**2 for i in range(len(y_new))]
        if sqrt(sum(e)) < eps:
            break
        k += 1
    
    answer = [f(i) for i in X]
    eps = [abs(y_new[i] - answer[i]) for i in range(X.shape[0])]
    if dr:
        print("Eps = {:6f} \n Количество итераций - {}".format(sqrt(sum(e)),k ))
        draw_k(X,y_new,answer,eps)
    return y_new



def draw_k(X,Y,A,E):
    print('______________________________')
    print('k |   x   |  y   |  y_tr| e   |')
    print('__|_______|______|______|_____|')
    for i in range(X.shape[0]):
        print("{} | {:.4f}|{:.4f}| {:.4f}| {:.4f}|"\
        .format(i,X[i],Y[i],A[i],E[i]))
    print('__|_______|______|______|_____|')
    

if __name__ == '__main__':
    X_0 = 0.
    X_k = 1.
    h_1 = .05
    eps = .1
    X = np.arange(X_0,X_k+h_1, h_1)
    A = konechno(X,h_1, dr = True)
    E = RRR(A,X,konechno,h_1,eps,4)
    print("Ошибка Рунге-Ромберга конечно-разностным методом \n ", E)
