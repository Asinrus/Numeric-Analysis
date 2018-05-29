import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log
import matplotlib.pyplot as plt
'''МНК через матрицу Грамма'''

def squad_method(X, y,n=1):
    F = []
    for i in range(n+1):
        temp = [j**i for j in X]
        F.append(temp)

    F = np.array(F,dtype = float).transpose()
    y = np.array(y,dtype = float)
    G = F.transpose() @ F 
    G_obr  = (np.linalg.inv(G))
    return G_obr @ F.transpose() @ y

def draw(X,y, c):
    point  = np.linspace(min(X),max(X),50)
    point_y = []
    s = 0
    err = []
    for x in point:
        for j in range(len(c)):
            s += c[j]* (x**j)
        point_y.append(s)
        s = 0
    
    for i in range(len(X)):
        for j in range(len(c)):
            s += c[j]* (X[i]**j)
        err.append( (y[i] - s)**2 )
        s = 0

    plt.plot(point,point_y, c ='r',label = 'МНК %d степени. Ошибка - %.5f'%(len(c)-1, sum(err)) )

if __name__ == '__main__':
    # 1 и 2 степени
    #X = [0,1.7,3.4,5.1,6.8,8.5]
    #y = [0.0,1.3038,1.8439,2.2583,2.6077,2.9155]
    X = [-5., -3.,-1., 1., 3., 5.]
    y = [-1.3734,-1.249,-0.7854,0.7854,1.249,1.3734]
    f_1 = squad_method(X,y)
    f_2 = squad_method(X,y,2)
    print("Коэффициенты при 1 степени : ",f_1)
    print("Коэффициенты при 2 степени : ", f_2)

    draw(X,y,f_1)
    draw(X,y,f_2)

    plt.scatter(X,y,label ='true')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Lab3_2')
    plt.show()
    
    