import numpy as np

def solver(A,n,EPS):
    from math import atan,sin,cos,sqrt,pi
    k = 0
    #добавить собственные векторы
    R = np.zeros((n,n),dtype = float)
    np.fill_diagonal(R,1)
    while sqrt( sum_non_diag(A) ) > EPS:
        max_a, i_a, j_a = get_max_elem_nondiag(abs(A))
        U = np.zeros((n,n),dtype = float)
        np.fill_diagonal(U,1)
        phi = 0.5*atan(2*max_a / (A[i_a,i_a] - A[j_a,j_a]) ) if A[i_a,i_a] != A[j_a,j_a]  else pi/4;
        U[i_a, j_a] = -sin(phi)
        U[j_a,i_a] = sin(phi)
        U[j_a,j_a] = cos(phi)
        U[i_a,i_a] = cos(phi)
        A = np.dot(np.dot(U.transpose(),A),U)
        R = R @ U
        k+=1
        
    l = np.diag(A)
    
    output.insert("0.0","\n end")
    output.insert("0.0",sqrt( sum_non_diag(A) ) )
    output.insert("0.0","\n погрешность= ")
    
    output.insert("0.0",k)
    output.insert("0.0","количество итераций= ")
    
    output.insert("0.0","\n")
    output.insert("0.0",R)
    output.insert("0.0","Собственные вектора= \n")
    
    output.insert("0.0","\n")
    output.insert("0.0",l)
    output.insert("0.0","Лямбда= \n")

    
def get_max_elem_nondiag(X):
    maximum = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                if maximum < X[i,j]:
                    maximum = X[i,j]
                    index_i, index_j = i,j
    return maximum, index_i, index_j

def sum_non_diag(X):
    s = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                s += (X[i,j]**2)
    return s
        
    
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
    file = open('file.txt','r')
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

