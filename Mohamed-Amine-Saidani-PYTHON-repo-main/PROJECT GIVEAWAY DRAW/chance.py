from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import load,dump
x=QApplication([])
w=loadUi("chance.ui")
w.show()

ch="29234560"
def premier(n):
    k=2
    while k<=n//2 and n%k!=0:
        k=k+1
    return k>n//2


def chance(x):
    s=0
    for i in range(len(x)):
        s=s+int(x[i])*i
        print(s)
    return premier(s)
        
    
    

def play():
    tel=w.tel.text()
    
    if(tel=="" or len(tel)!=8 ):
        QMessageBox.critical(w,"error","Please enter your number")
    elif not(tel[0] in ["2","4","5","9"]):
        QMessageBox.critical(w,"error","The first digit must be 2 or 4 or 5 or 9")
    
    elif chance(tel)==True:
        
        x1="Congratulations you won the giveaway"
        w.res.setText(str(x1))
    
    else:
        x2="sorry,good luck next time"
        w.res.setText(str(x2))
    





w.bt1.clicked.connect(play)


x.exec_()