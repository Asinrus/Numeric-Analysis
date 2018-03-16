def solver(A,B,n):
    P=np.zeros(n)
    Q=np.zeros(n)
    P[0]=-A[0,1]/A[0,0]
    Q[0]=B[0] /A[0,0]
    for i in range(1,n-1):
        a,b,c,d = A[i,i-1],A[i,i],A[i,i+1],B[i]
        P[i]=-c / (b+a*P[i-1])
        Q[i]=(d-a*Q[i-1]) / (b+a*P[i-1])
    Q[-1]=(B[-1] - A[-1,-2]*Q[-2]) / (A[-1,-1]+A[-1,-2]*P[-2])
    X=np.zeros(n)
    X[-1]=Q[-1]
    for i in range(n-2,-1,-1):
        X[i]=P[i]*X[i+1]+Q[i]

    output.insert("0.0","\n")
    output.insert("0.0",X)
    output.insert("0.0","X= \n")
    
    output.insert("0.0","\n")
    output.insert("0.0",Q)
    output.insert("0.0","Q= \n")
    
    output.insert("0.0","\n")
    output.insert("0.0",P)
    output.insert("0.0","P= \n")
    
    
def handler():
    output.delete('1.0',END)
    try:
        # make sure that we entered correct values
        A = np.array([a[i].get() for i in range(n*n)],dtype=float).reshape(n,n)
        B = np.array([b[i].get() for i in range(n)],dtype=float)
        solver(A, B,n)
    except ValueError:
        output.insert("0.0","Make sure you entered all values\n")

from tkinter import *
import numpy as np

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

n=5
a =[Entry(frame, width=5) for _ in range(n*n)]
b= [Entry(frame, width=5) for _ in range(n)]
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

but = Button(frame, text="Solve", command=handler).grid(row=n+2, column=2*n, padx=(10,0))
 
# место для вывода решения уравнения
output = Text(frame, bg="lightblue", font="Arial 8", width=70, height=30)
output.grid(row=6, columnspan=8)
 
# запускаем главное окно
root.mainloop()

