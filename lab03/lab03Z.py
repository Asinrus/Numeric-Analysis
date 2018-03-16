import numpy as np
def solver(A,B,n,EPS):
    it = 0
    alpha = np.zeros((n,n),dtype = float)
    for i in range(n):
        for j in range(n):
            alpha[i][j] = -A[i,j]/A[i,i] if i!=j else 0
        B[i] = B[i] / A[i,i]
    
    c = [alpha[i,j] if j >= i else 0 for i in range(n)
        for j in range(n)]

    c = np.array(c).reshape(n,n)
    
    norma_a = norma(np.abs(alpha))
    norma_c = norma(np.abs(c))
    koef = norma_c / (1 - norma_a)
    x_0 = np.zeros(n,dtype = float)  
    x_1 = np.zeros(n, dtype = float) + [x for x in B]
    
    while koef * norma(np.abs(x_0 - x_1)) > EPS:
        x_0 =[x for x in x_1]
        for i in range(n):
            x_1[i] = B[i] + np.dot(alpha[i,:], x_1) 
        it+=1
        
        
    output.insert("0.0","\nend\n")
    output.insert("0.0",koef * norma(np.abs(x_0 - x_1)) )
    output.insert("0.0","погрешность= ")
    
    output.insert("0.0","\n")
    output.insert("0.0",it)
    output.insert("0.0","количество итераций= ")
    
    output.insert("0.0","\n")
    output.insert("0.0",x_0)
    output.insert("0.0","X= \n")
   
    output.insert("0.0","\n")
    output.insert("0.0",alpha)
    output.insert("0.0","alpha= \n")
    
    output.insert("0.0","\n")
    output.insert("0.0",A)
    output.insert("0.0","A= \n")
        
def norma(X):
    a = np.zeros(n,dtype = float)
    for i in range(n):
        a[i] = np.sum(X[i])
    return np.max(a)        
    
def handler():
    output.delete('1.0',END)
    try:
        # make sure that we entered correct values
        A = np.array([a[i].get() for i in range(n*n)],dtype=float).reshape(n,n)
        B = np.array([b[i].get() for i in range(n)],dtype=float)
        EPS = float(eps.get())
        solver(A, B,n,EPS)
    except ValueError:
        output.insert("0.0","Make sure you entered all values\n")
        
def load():
    file = open('file.txt','r')
    k=0
    eps.delete(0,END)
    eps.insert(0,float(file.readline()))
    for line in file:
        l = list(map(float,line.split()))
        if k < n*n:
            for i in range(len(l)):
                a[k].delete(0,END)
                a[k].insert(0,l[i])
                k+=1
        else:
             for i in range(len(l)):
                b[i].delete(0,END)
                b[i].insert(0,l[i])
        
    file.close()

from tkinter import *

np.set_printoptions(precision = 3)
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

n=4
a =[Entry(frame, width=5) for _ in range(n*n)]
b= [Entry(frame, width=5) for _ in range(n)]
eps = Entry(frame, width=6)
eps.grid(row=n+1,column = n*2+2)
eps.insert(0,0.01)
eps_lab = Label(frame, text = "Погрешность = ").grid(row=n+1, column = n*2+1)
lab=[] 
k=0 
for i in range(n):
    for j in range(n):
        a[k].grid(row= i+1,column= 2*j)
        a[k].insert(k,0)
        lab.append(Label(frame, text = "x{}+".format(j+1)).grid(row=i+1, column = 2*j+1))
        k+=1
      
for i in range(n):
    b[i].grid(row = i+1, column=n*2+1)
    lab.append(Label(frame, text = "=").grid(row=i+1, column = n*2)) 

# кнопка решить

but = Button(frame, text="Solve", command=handler).grid(row=n+2, column=2*n+2, padx=(10,0))
but = Button(frame, text="Load", command=load).grid(row=n+3, column=2*n+2, padx=(10,0)) 
 
# место для вывода решения уравнения
output = Text(frame, bg="lightblue", font="Arial 10", width=70, height=30)
output.grid(row=6, columnspan=8)
 
# запускаем главное окно
root.mainloop()

