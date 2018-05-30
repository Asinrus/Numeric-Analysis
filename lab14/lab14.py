
#Метод стрельбы и конечно-разностный
import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log,tan,e
import matplotlib.pyplot as plt

#ОДУ 1-го порядка 
def f_el_y(x,y):
    return x

def f_el_z(x,y,z):
    return z * (2*x+1)/x - (x+1)/x * y

def f(x):
    return (e**x) * x

def RRR(A,X_old,f,h,eps,p):
    X_0 = 1.
    X_k = 2.
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


def shot(X,h,eps,dr = False):
    a_old = 0
    a_new = 0.01

    it = 1
    X,Y,Z,dY,dZ,A,E = runge_kutta_1(a_old,X,h)
    F1 = Z[-1] - 2*Y[-1]
    if abs(F1) <= eps:
        a = a_old
    else: 
        X1,Y1,Z1,dY1,dZ1,A1,E1 = runge_kutta_1(a_new,X,h)
        F2 = Z1[-1] - 2*Y1[-1]
        if abs(F2)<=eps:
            a = a_new
        else:
            while abs(F2) > eps and it < 1000:
                a = a_new -(a_new - a_old)*F2 / (F2 - F1)
                X,Y,Z,dY,dZ,A,E = runge_kutta_1(a,X,h)
                F1 = F2 + 1 - 1
                F2 = Z[-1] - 2*Y[-1]
                a_old = a_new + 1 - 1
                a_new = a + 1 - 1
                it += 1
    print("Метод стрельбы c шагом {:.2f} сошелся за {} с y0 = {:.7f}\n погрешность = {:.7f}".format(h,it,a,abs(F2)))
    
    X,Y,Z,dY,dZ,A,E = runge_kutta_1(a,X,h)
    if dr:
        draw(X,Y,Z,dY,dZ,A,E)
    return Y

def konechno(X,h,eps= 0,dr = False):
    n = X.shape[0]
    A = np.zeros((n,n),dtype = float)
    B = np.zeros(n,dtype = float)
    answer = []
    B[0] = 3*h*e
    A[0][0], A[0][1] = -1.,1
    for i in range(1,n-1):
        A[i][i-1] = 1/(h*h) + (2*X[i] + 1) / X[i] /2 /h
        A[i][i] = -2/(h*h) + (X[i] + 1) / X[i]
        A[i][i+1] = 1/(h*h) - (2*X[i] + 1) / (X[i]*2*h)
    A[-1][-2], A[-1][-1] = -1 , 1-2*h
    y = np.linalg.solve(A, B)
    answer = [f(i) for i in X]
    eps = [abs(y[i] - answer[i]) for i in range(X.shape[0])]
    if dr:
        draw_k(X,y,answer,eps)
    return y


def runge_kutta_1(a,X,h):
    Y=[a]
    Z=[3*e]
    A = [f(X[0])]
    dY = [0]
    dZ = [0]
    E = [0]

    y = Y[0]
    z = Z[0]

    for x in X[1:]:
        K_1 = h * f_el_y(z,y)
        K_2 = h * f_el_y(z + 0.5*h,y+0.5*K_1)
        K_3 = h * f_el_y(z + 0.5*h,y+0.5*K_2)
        K_4 = h * f_el_y(z + h, y + K_3)

        dy = 1/6 * (K_1 + 2*K_2 + 2*K_3 + K_4)
        temp_y = y + dy

        K_1_z = h * f_el_z(x,y,z)
        K_2_z = h * f_el_z(x + 0.5*h,y+0.5*K_1,z+0.5*K_1_z)
        K_3_z = h * f_el_z(x + 0.5*h,y+0.5*K_2,z+0.5*K_2_z)
        K_4_z = h * f_el_z(x + h, y + K_3,z + K_3_z)

        dz = 1/6 * (K_1_z + 2*K_2_z + 2*K_3_z + K_4_z)
        temp_z = z + dz
    
        Y.append(temp_y)
        Z.append(temp_z)
        A.append(f(x))
        dY.append(dy)
        dZ.append(dz)
        E.append(abs( temp_y - A[-1]) )

        y = Y[-1]
        z = Z[-1]

    return X,Y,Z,dY,dZ,A,E

def draw_k(X,Y,A,E):
    print('______________________________')
    print('k |   x   |  y   |  y_tr| e   |')
    print('__|_______|______|______|_____|')
    for i in range(X.shape[0]):
        print("{} | {:.4f}|{:.4f}| {:.4f}| {:.4f}|"\
        .format(i,X[i],Y[i],A[i],E[i]))
    print('__|_______|______|______|_____|')
    

def draw(X,Y,Z,dY,dZ,A,E):
    print('_______________________________________________________')
    print('k |   x   |  y   |  z    |  d_z   |  d_y  |  y_tr| e   |')
    print('__|_______|______|_______|________|_______|______|_____|')
    for i in range(len(X)):
        print("{} | {:.4f}|{:.4f}| {:.4f}| {:.4f}| {:.4f}|{:.4f}|{:.4f}|"\
        .format(i,X[i],Y[i],Z[i],dZ[i],dY[i],A[i],E[i]))
    print('__|_______|______|_______|________|_______|______|_____|')


if __name__ == '__main__':
    X_0 = 1.
    X_k = 2.
    h_1 = .1
    eps = .001
    X = np.arange(X_0,X_k+h_1, h_1)
    A = shot(X,h_1,eps,dr = True)
    E = RRR(A,X,shot,h_1,eps,4)
    print("Ошибка Рунге-Ромберга методом стрельбы \n ", E)
    A = konechno(X,h_1, dr = True)
    E = RRR(A,X,konechno,h_1,eps,4)
    print("Ошибка Рунге-Ромберга конечно-разностным методом \n ", E)



