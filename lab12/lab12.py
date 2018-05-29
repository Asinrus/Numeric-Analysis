import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log
import matplotlib.pyplot as plt
'''Численное интегрирование методом прямоугольников, трапеций, Симпсона'''
def f(x):
    return x*x / (x*x+16)

# метод прямоугольников
def pr(h,X):
    s = 0
    for i in range(len(X)-1):
        s += f( 0.5*(X[i] + X[i+1]) )
    
    return s*h

#метод трапеций
def tr(h,X):

    s = f(X[0])/2
    for i in range(1,len(X)-1):
        s += f(X[i])
    
    s += f(X[len(X)-1])/2

    return s*h

#метод Симпсона
def simps(h,X):
    s = f(X[0])
    for i in range(1,len(X)-1):
        if i % 2 == 1:
            s += 4*f(X[i])
        else:
            s += 2*f(X[i])
    
    s += f(X[len(X)-1])

    return h/3 *s

def RRR(h1,F,h2,F_k):
    k = h1 / h2
    return F + (F - F_k ) / (k**2 - 1)

def eps(F1,F2,p):
    return abs((F1 - F2) / (2 **p - 1))
    
#методами прямоугольников, трапеций, Симпсона с шагами 
if __name__ == '__main__':
    X_0 = 0.
    X_k = 2.
    h_1 = .5
    h_2 = .25
    X_1 = np.arange(X_0,X_k+h_1, h_1)
    X_2 = np.arange(X_0,X_k+h_2, h_2)
    print("Интегрирование методом прямоугольником с шагом {} = {:.7f}".format(h_1,pr(h_1,X_1)))
    print("Интегрирование методом прямоугольником с шагом {} = {:.7f}".format(h_2,pr(h_2,X_2)))
    R = eps (pr(h_2,X_2) , pr(h_1,X_1), 1)
    print ("Метод Рунге-Ромберга-Ричардсона = {} \n".format(R))

    print("Интегрирование методом трапеций с шагом {} = {:.7f}".format(h_1,tr(h_1,X_1)))
    print("Интегрирование методом трапеций с шагом {} = {:.7f}".format(h_2,tr(h_2,X_2)))
    R = eps (tr(h_2,X_2) , tr(h_1,X_1),2)
    print ("Метод Рунге-Ромберга-Ричардсона = {} \n".format(R))

    print("Интегрирование методом Симпсона с шагом {} = {:.7f}".format(h_1,simps(h_1,X_1)))
    print("Интегрирование методом Симпсона с шагом {} = {:.7f}".format(h_2,simps(h_2,X_2)))
    R =  R = eps (simps(h_2,X_2) , simps(h_1,X_1),4)
    print ("Метод Рунге-Ромберга-Ричардсона = {} \n".format(R))


