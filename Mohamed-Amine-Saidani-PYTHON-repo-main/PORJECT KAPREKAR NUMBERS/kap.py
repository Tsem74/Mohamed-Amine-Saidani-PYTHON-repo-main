from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import load,dump

x=QApplication([])
w=loadUi("kap.ui")
w.show()

def kap(k):
    c=len(k)
    ch=str(int(k)*int(k))
    j=len(ch)-c
    return int(ch[j:len(ch)])+int(ch[:j])==int(k)
        


def valider():
    n=w.n.text()
    if(n=="" or n.isdecimal()==False):
        QMessageBox.critical(w,"error","Invalid Number")
    else:
        if(kap(str(n))):
            w.res.setText(str('This is a Kaprekar number with a Factorial of:'+str(fact(int(n)))))
        else :
            w.res.setText(str("This is not a Kaprekar number, its Factorial is: "+str(fact(int(n)))))

def fact(i):
    if(i==0):
        return 1
    else:
        return i*fact(i-1)
    return i



w.bt1.clicked.connect(valider)

x.exec_()