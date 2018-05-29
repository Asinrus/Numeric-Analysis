import sys
import numpy as np
from math import sin, pi,cos,sqrt,asin
from PyQt5.QtWidgets import (QApplication, QWidget,\
QPushButton, QToolTip,QTextEdit,QMainWindow,QAction,QLabel,QVBoxLayout,\
QDoubleSpinBox)

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


'''Решение системы нелинейыъ уравнений методом Ньютона . 
Проблема в методе простой итерации не смог подобрать коэффициент '''
class NewtoneMethod:
    a=1
    A = 0
    B = pi/2 
    x0 = A
    def f_1(self,x1,x2):
        return x1-cos(x2)-self.a

    def f_2(self,x1,x2):
        return x2-sin(x1)-self.a
    
    def det_J(self,x1,x2):
        return 1+sin(x2)*cos(x1)

    def A_1(self,x1,x2):
        return self.f_1(x1,x2) - self.f_2(x1,x2) * sin(x2)

    def A_2(self,x1,x2):
        return self.f_2(x1,x2) + self.f_1(x1,x2) * cos(x1)

    
    
    def solver(self,eps):
        x = [0,0]
        x_k = [0,0]
        it = 0
        while True:
            x_k[0] = x[0] - self.A_1(x[0],x[1]) / self.det_J(x[0],x[1])
            x_k[1] = x[1] - self.A_2(x[0],x[1]) / self.det_J(x[0],x[1])
            it += 1
            if max( abs(x_k[0]-x[0]) ,abs(x_k[1]-x[1]) ) < eps or it >100:
                break 
            x[:] = [i for i in x_k]

        s = "Newton \n Answer \n x1 =  %.4f \n x2 = %.4f \n Iteration %d \n Eps %.9f,\n f1(x1,x2) = %.4f \n f2(x1,x2) = %.4f \n"\
         %(x_k[0],x_k[1], it, max( abs(x_k[0]-x[0]) ,abs(x_k[1]-x[1])), self.f_1(x_k[0],x_k[1]),self.f_2(x_k[0],x_k[1]))  
        return s


class Iteration(NewtoneMethod) :


    def phi_1(self,x):
        return cos(x) + self.a
    
    def phi_2(self,x):
        return sin(x) + self.a
    
    def solver(self,eps):
        q = 0.5
        eps_q = abs(q/(1-q))
        print(eps_q)
        it = 0
        x = [0,0]
        x_k = [0,0]
        while True:
            x_k[0] = self.phi_1(x[1])
            x_k[1] = self.phi_2(x[0])
            it += 1
            if eps_q* max( abs(x_k[0]-x[0]) ,abs(x_k[1]-x[1]) ) < eps or it >100:
               break
            x[:] = [i for i in x_k]
        s = "Simple \n Answer \n x1 =  %.4f \n x2 = %.4f \n Iteration %d \n Eps %.9f,\n f1(x1,x2) = %.4f \n f2(x1,x2) = %.4f \n"\
         %(x_k[0],x_k[1], it, eps_q*max( abs(x_k[0]-x[0]) ,abs(x_k[1]-x[1])), self.f_1(x_k[0],x_k[1]),self.f_2(x_k[0],x_k[1]))  
        return s
            
        
    
class Window(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def pr(self,eps):
        newtone = NewtoneMethod()
        simple = Iteration()
        self.answer.setText("")
        self.answer.insertPlainText(newtone.solver(eps))
        self.answer.insertPlainText(simple.solver(eps))


    def initUI(self):
        
        label_eps = QLabel("Eps: ")
        eps = QDoubleSpinBox()
        eps.setDecimals(4)
        eps.setFixedSize(80,32)
        eps.setRange(0.0001,1)
        eps.setSingleStep(0.01)
        eps.setValue(0.01)

        label_answer = QLabel("Answer:  ")
        self.answer = QTextEdit()
        self.answer.setFixedSize(300,300)
        self.setToolTip("WINDOWS")
        button = QPushButton("Solve", self)
        button.setFixedSize(64,32) 
        button.clicked.connect(lambda:self.pr(eps.value()))
        button.setToolTip("Button")

        layout = QVBoxLayout();
        layout.addWidget(label_eps)
        layout.addWidget(eps)
        layout.addWidget(button)
        layout.addWidget(label_answer)
        layout.addWidget(self.answer)


        self.setGeometry(300,300,300,200)
        self.setLayout(layout)
        self.setWindowTitle("Lab07")
        self.show()
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())