import numpy as np
from math import sqrt,fabs


def solver(A,n,eps):
    k = 0
    R = np.array(A)
    it = 0
    
    while 1:
        it += 1
        Q = np.eye(n)
        e_k = 0
        
        for j in range(n - 1):
            v = np.zeros(n)
            v[j] = A[j][j] + np.sign(A[j][j]) * ((norm(np.transpose(A)[j], j)))    
            for i in range(j + 1, n):
                v[i] = A[i][j]
            H = np.eye(n) - 2 * (mult(v)) / np.dot(v, v)
            Q = np.dot(Q, H)
            A = np.dot(H, A)
        
        A = np.dot(A, Q)
        for m in range(1, n):
            e_k += A[m][0] ** 2
            
        e_k = sqrt(e_k)
        if e_k < eps:
           break
           
    D = ((A[1][1] + A[2][2]) ** 2 - 4 * (A[1][1] * A[2][2] - A[1][2] * A[2][1]))
    l = []
    if D >= 0:
        for i in range(n):
            l.append("x{} {}\n".format(i + 1, A[i][i]))
    else:
        l.append("x1 {}\n".format(A[0][0]))
        l.append("x2 {}\n".format(complex((A[1][1] + A[2][2])/2,
                             sqrt(fabs(D))/2)))   
        l.append("x3 {}\n".format(complex((A[1][1] + A[2][2])/2,
                             -sqrt(fabs(D))/2)))

        
    output.insert("0.0","\nend\n")    
    for i in range(len(l)-1,-1,-1):
            output.insert("0.0",l[i] )
            
    output.insert("0.0","\n")
    output.insert("0.0",e_k )
    output.insert("0.0","погрешность= ")    

    output.insert("0.0","\n")
    output.insert("0.0",it)
    output.insert("0.0","количество итераций= ")

    
def norm(vec, i):
    res = 0
    for j in range(i, n):
        res += vec[j] ** 2
    return sqrt(res)

def mult(a):
    first = np.zeros((n, n))
    first[0] = a
    return np.dot(np.transpose(first), first)

    
    
    
def handler():
    output.delete('1.0',END)
    try:
        # make sure that we entered correct values
        A = np.array([a[i].get() for i in range(n*n)],dtype=float).reshape(n,n)
        EPS = float(eps.get())
        solver(A,n,EPS)
    except ValueError:
        output.insert("0.0","Make sure you entered all values\n")
        
def load():
    file = open('file1.txt','r')
    k=0
    eps.delete(0,END)
    eps.insert(0,float(file.readline()))
    for line in file:
        l = list(map(float,line.split()))
        for i in range(len(l)):
            a[k].delete(0,END)
            a[k].insert(0,l[i])
            k+=1
    file.close()
    
        
from tkinter import *

np.set_printoptions(precision = 5)
# родительский элемент
root = Tk()
# устанавливаем название окна
root.title("Matrix")
# устанавливаем минимальный размер окна 
root.minsize(240,600)
# выключаем возможность изменять окно
root.resizable(width=True, height=True)
 
# создаем рабочую область
frame = Frame(root)
frame.grid()

n=3
a =[Entry(frame, width=5) for _ in range(n*n)]
eps = Entry(frame, width=6)
eps.grid(row=n,column = n+1)
eps.insert(0,0.3)
eps_lab = Label(frame, text = "Погрешность = ").grid(row=n, column = n)
lab=[] 
k=0 
Label(frame, text = "Собственные значения").grid(row = 0,column = 0)
for i in range(n):
    for j in range(n):
        a[k].grid(row= i+1,column= j)
        k+=1
# кнопка решить

but = Button(frame, text="Solve", command=handler).grid(row=n-1, column=n+2, padx=(10,0))
but = Button(frame, text="Load", command=load).grid(row=n, column=n+2, padx=(10,0)) 
# место для вывода решения уравнения
output = Text(frame, bg="lightblue", font="Arial 10", width=70, height=30)
output.grid(row=6, columnspan=8)
 
# запускаем главное окно
root.mainloop()

