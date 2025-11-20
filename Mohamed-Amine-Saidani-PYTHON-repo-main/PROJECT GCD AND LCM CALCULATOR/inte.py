from PyQt5.uic import*
from PyQt5.QtWidgets import*
x=QApplication([])
w=loadUi('interface.ui')
w.show()

def pgcd(a,b):
    if(a==b):
        return a
    elif a>b:
        return pgcd(a-b,b)
    else:
        return pgcd(a,b-a)
def ppcm(a,b):
    x=a
    y=b
    while(x!=y):
        if(x<y):
            x=x+a
        else:
            y=y+b
    return x

def calculer(a,b):
    w.pg2.clear()
    w.pp2.clear()
    if(w.pg1.isChecked()):
        w.pg2.setText(str(pgcd(a,b)))
    if(w.pp1.isChecked()):
        w.pp2.setText(str(ppcm(a,b)))
        
def play():
    a=w.a.text()
    b=w.b.text()
    if(a=="" or b==""):
        QMessageBox.critical(w,'error','Please enter two numbers')
    elif(a.isdecimal()==False or b.isdecimal()==False ):
        QMessageBox.critical(w,'error','invalid value')
    elif(w.pg1.isChecked()==False and w.pp1.isChecked()==False ):
        QMessageBox.critical(w,'error','please select an operation')
    else:
        calculer(int(a),int(b))
        
def effacer():
    w.a.clear()
    w.b.clear()
    w.pg2.clear()
    w.pp2.clear()
    w.pg1.setChecked(False)
    w.pp1.setChecked(False)










w.bt1.clicked.connect(play)
w.bt2.clicked.connect(effacer)

x.exec_()