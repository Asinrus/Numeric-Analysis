import numpy as np
from math import sin, pi,cos,sqrt,asin,atan,log
import matplotlib.pyplot as plt

'''Сплайн-интерполяция. Решение с использование метода прогонки'''


def h(X,i):
    return X[i]-X[i-1]

def form_b(X,f):
    b = []
    for i in range(2,len(X)):
        temp = 3* ( (f[i]-f[i-1])/h(X,i) - (f[i-1] - f[i-2])/h(X,i-1) )
        b.append(temp)
    return b

def form_a(X):
    A = np.zeros((len(X)-2,len(X)-2),dtype = float)
    A[0,0]=2*(h(X,1)+h(X,2))
    A[0,1] = h(X,2)

    for i in range(1,len(X)-2):
        A[i,i-1] = h(X,i)
        A[i,i] = 2* ( h(X,i)+h(X,i+1) )
        if i != len(X)-3:
            A[i,i+1] = h(X,i+1)
    return A

def form_another(X,f,c):
    b, d = [], []
    for i in range(len(X)-2):
        temp_b = 1/h(X,i+1) * (f[i+1] - f[i]) - 1/3 * h(X,i+1) *(c[i+1] + 2*c[i])
        b.append(temp_b)
        
        temp_d = (c[i+1] - c[i]) / 3 / h(X,i+1)
        d.append(temp_d)
    
    n = len(X)-2
    temp_b = 1/ h(X,n+1) * (f[n+1] - f[n]) - 2/3 * h(X,n+1) * c[n]
    b.append(temp_b)

    temp_d = - c[n] / (3* h(X,n))
    d.append(temp_d)

    return b,d

class Spline :
    
    def tridiag_matrix(self,A,B,n):
        P=np.zeros(n)
        Q=np.zeros(n)
        P[0]=-A[0,1]/A[0,0]
        Q[0]=B[0] /A[0,0]
        for i in range(1,n-1):
            a,b,c,d = A[i,i-1],A[i,i],A[i,i+1],B[i]
            P[i]=-c / (b+a*P[i-1])
            Q[i]=(d-a*Q[i-1]) / (b+a*P[i-1])
        Q[-1]=(B[-1] - A[-1,-2]*Q[-2]) / (A[-1,-1]+A[-1,-2]*P[-2])
        x=np.zeros(n)
        x[-1]=Q[-1]
        for i in range(n-2,-1,-1):
            x[i]=P[i]*x[i+1]+Q[i]
        return x

    def solver(self,X,f):

        n = len(X)-2
        c = np.zeros(n,dtype = float)
        A = form_a(X)
        B = form_b(X,f)
        
        self.c = np.concatenate(([0],self.tridiag_matrix(A,B,n)))
        self.a = np.array(f[:-1])
        self.b,self.d  = form_another(X,f,self.c)
        self.broader = [ (X[i],X[i+1]) for i in range(len(X)-1) ]
        self.X,self.f = X,f
    
    def value(self, x):
        for j,(right,left) in enumerate(self.broader):
            if right <= x <= left:
                i = j

        return self.a[i]+self.b[i]*(x-self.X[i])+self.c[i]*(x-self.X[i])**2+self.d[i]*(x- self.X[i])**3
        



if __name__ == '__main__':
    X_0 = -0.5
    X_i = [-3.,-1.,1.,3.,5.]
    f_i = [-1.249,-0.7854,.7845,1.249,1.3734]
    solver = Spline()
    solver.solver(X=X_i,f = f_i)
    print('Функция в точке {} = {}'.format(X_0,solver.value(X_0)))
    X = np.linspace(-3., 5., 100)
    y=[]
    for j in X:
        y.append(solver.value(j))

    plt.plot(X,y,label ='spline')
    plt.scatter(X_i,f_i, c ='g',label = 'true' )
    plt.scatter(X_0,solver.value(X_0),c = 'r',label = 'dot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Lab3_2')
    plt.show()