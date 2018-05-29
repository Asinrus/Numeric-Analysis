import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log,tan
import matplotlib.pyplot as plt

#ОДУ 1-го порядка 

def RRR(A,X_old,f, h,p):
    X_0 = 0.
    X_k = 1.
    h_1 = 2*h
    X = np.arange(X_0,X_k+h_1, h_1)
    _,dA,_,_,_,_,_ = f(X,h_1)
    E = []
    for i in range(len(X)):
        if X[i] in X_old:
            j = list(X_old).index(X[i])
            error = abs(dA[i] - A[j]) / (2**p-1)
            E.append(error)
    return E

def RRRA(A,X_old,f, h,p):
    X_0 = 0.
    X_k = 1.
    h_1 = 2*h
    X = np.arange(X_0,X_k+h_1, h_1)
    _,dA,_,_,_  = f(X,h_1)
    E = []
    for i in range(len(X)):
        if X[i] in X_old:
            j = list(X_old).index(X[i])
            error = abs(dA[i] - A[j]) / (2**p-1)
            E.append(error)
    return E

def f_el_y(x,y):
    return x

def f_el_z(x,y,z):
    return -z*tan(x) - y * (cos(x)**2)

def f(x):
    return cos(sin(x)) + sin(cos(x))
def adams(X,h):
    Y=[1+sin(1)]
    Z=[0]
    A = [f(0)]
    dY = [0]
    dZ = [0]
    E = [abs( Y[-1] - A[-1])]

    y = Y[0]
    z = Z[0]

    for i in range(3):
        x = X[i]
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
        E.append(abs( temp_y - A[-1]) )

        y = Y[-1]
        z = Z[-1]
    for i in range(3,len(X)):
        x = X[i]
        temp_y = y + h/24*(55*f_el_y(Z[i],Y[i]) - 59*f_el_y(Z[i-1],Y[i-1])+ 37*f_el_y(Z[i-2],Y[i-2]) - 9*f_el_y(Z[i-3],Y[i-3]) )
        temp_z = z + h/24*(55*f_el_z(X[i],Y[i],Z[i]) - 59*f_el_z(X[i-1],Y[i-1],Z[i-1])+37*f_el_z(X[i-2],Y[i-2],Z[i-2]) - 9*f_el_z(X[i-3],Y[i-3],Z[i-3]))

        Y.append(temp_y)
        Z.append(temp_z)
        A.append(f(x))
        E.append(abs( temp_y - A[-1]) )

        y = Y[-1]
        z = Z[-1]


    
    return X,Y,Z,A,E


def runge_kutta_1(X,h):
    Y=[1+sin(1)]
    Z=[0]
    A = [f(0)]
    dY = [0]
    dZ = [0]
    E = [abs( Y[-1] - A[-1])]

    y = Y[0]
    z = Z[0]

    for x in X:
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

def elyar_1(X,h):
    Y=[1+sin(1)]
    Z=[0]
    A = [0]
    dY = [0]
    dZ = [0]
    E = [abs( Y[-1] - A[-1])]

    y = Y[0]
    z = Z[0]

    for x in X:
        temp_y = y + h*f_el_y(z,y)
        temp_z = z + h*f_el_z(x,y,z)

        Y.append(temp_y)
        Z.append(temp_z)
        A.append(f(x))
        dY.append(h*f_el_y(x,y))
        dZ.append(h*f_el_z(x,y,z))
        E.append(abs( temp_y - A[-1]) )

        y = Y[-1]
        z = Z[-1]
    return X,Y,Z,dY,dZ,A,E

def draw(X,Y,Z,dY,dZ,A,E):
    print('_______________________________________________________')
    print('k |   x   |  y   |  z    |  d_z   |  d_y  |  y_tr| e   |')
    print('__|_______|______|_______|________|_______|______|_____|')
    for i in range(len(X)):
        print("{} | {:.4f}|{:.4f}| {:.4f}| {:.4f}| {:.4f}|{:.4f}|{:.4f}|"\
        .format(i,X[i],Y[i],Z[i],dZ[i],dY[i],A[i],E[i]))
    print('__|_______|______|_______|________|_______|______|_____|')

def draw_adams(X,Y,Z,A,E):
    print('_______________________________________')
    print('k |   x   |  y   |  z    |  y_tr |  e  |')
    print('__|_______|______|_______|_______|_____|')
    for i in range(len(X)):
        print("{} | {:.4f}|{:.4f}| {:.4f}| {:.4f}|{:.4f}|"\
        .format(i,X[i],Y[i],Z[i],A[i],E[i]))
    print('__|_______|______|_______|_______|_____|')

if __name__ == '__main__':
    X_0 = 0.
    X_k = 1.
    h_1 = .1
    #h_1 = float(input("Введите шаг сетки :"))
    X = np.arange(X_0,X_k+h_1, h_1)
    print("Метод Эйлера:") 
    _,Y,Z,dY,dZ,A,E = elyar_1(X,h_1)
    draw(X,Y,Z,dY,dZ,A,E)
    error = RRR(Y,X,elyar_1,h_1,1)
    print("Ошибка Рунге-Ромберга ", error)

    print("Метод Рунге-Кутта:") 
    _,Y,Z,dY,dZ,A,E = runge_kutta_1(X,h_1)
    error = RRR(Y,X,runge_kutta_1,h_1,4)
    draw(X,Y,Z,dY,dZ,A,E)
    print("Ошибка Рунге-Ромберга ", error)

    print("Метод Адамса:") 
    _,Y,Z,A,E = adams(X,h_1)
    error = RRRA(Y,X,adams,h_1,4)
    draw_adams(X,Y,Z,A,E)
    print("Ошибка Рунге-Ромберга ", error)


