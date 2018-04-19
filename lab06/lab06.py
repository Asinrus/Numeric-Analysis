import sys
import numpy as np
from math import sin, pi,cos,sqrt,asin
from PyQt5.QtWidgets import (QApplication, QWidget,\
QPushButton, QToolTip,QTextEdit,QMainWindow,QAction,QLabel,QVBoxLayout,\
QDoubleSpinBox)

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class NewtoneMethod:
    A = -pi/2
    B = 0 
    x0 = A
    def f(self,x):
        return sin(x)-2*x*x + 0.5

    def df(self,x):
        return cos(x)-4*x

    def ddf(self,x):
        return -sin(x)
    
    def solver(self,eps):
        x_k = self.x0 - self.f(self.x0)/self.df(self.x0)
        x = self.x0
        it = 1
        self.self = self
        while(abs(x_k-x)>eps):
            x = x_k
            try:
                x_k = x - self.f(x)/self.df(x)
            except ZeroDivisionError:
                x_k = x - 0.00001
            if x_k >= self.B:
                return "Newtone \n Answer don't find \n"
            it += 1
        return "Newton \n Answer %.4f \n Iteration %d \n Eps %.7f,\n Function:  %.7f\n"\
         %(x_k, it,abs(x_k-x),self.f(x_k))


class Iteration(NewtoneMethod) :
    A = -pi/2
    B = 0
    x0 = A
    lam = 1/(2*pi+1)

    def phi(self,x):
        return x - self.lam*self.f(x)
    
    def solver(self,eps):
        if self.f(self.A) > 0 and  self.f(self.B) > 0 or self.f(self.A) < 0 and  self.f(self.B) < 0:
            print('Значения функций имеют один знак на указаных границах')
            exit(False)
        q = 1-2*pi*self.lam
        #q = 0.3
        eps_q = abs(q/(1-q))
        print(eps_q)
        it = 0
        x = self.x0
        x_k = self.phi(x)
        while eps_q*abs(x_k - x) >eps and it<100:
           x = x_k
           x_k = self.phi(x)
           it += 1

        return "Simple Iteration \n Answer %.4f \n Iteration %d \n Eps %.7f,\n Function: %.7f\n"\
         %(x_k, it,abs(eps_q*abs(x_k-x)),self.f(x_k))
            
        
    
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
        eps.setFixedSize(80,32)
        eps.setRange(0.001,1)
        eps.setSingleStep(0.01)
        eps.setValue(0.001)

        label_answer = QLabel("Answer:  ")
        self.answer = QTextEdit()
        self.answer.setFixedSize(300,100)
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
        self.setWindowTitle("Lab06")
        self.show()
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())