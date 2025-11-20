from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import load,dump

x=QApplication([])
w=loadUi("compte.ui")
w.show()

def puis(a,b):
    if (b==0):
        return 1
    else:
        return a*puis(a,b-1)

def baseb(n,b):
    ch=""
    while n!=0:
        if(n%b<9):
            ch=str(n%b)+ch
        else:
            ch=chr(n%b+55)+ch
        n=n//b
    return ch

def DECIMAL(ch,b):
    s=0
    for i in range(len(ch)):
        if("0"<=ch[i]<="9"):
            s=s+int(ch[i])*puis(b,len(ch)-1-i)
        else:
            s=s+(ord(ch[i])-55)*puis(b,len(ch)-1-i)
    return s
            


def premier(n):
    k=2
    while k<=n//2 and n%k!=0:
        k=k+1
    return k>n//2

def pgd(n):
    maxi=0
    for i in range(1,n+1):
        if (n%i==0 and premier(i) and maxi<i):
            maxi=i
    return maxi


def mdp(n,pr):
    ch=n[:4]+pr[:4]
    s=""
    for i in range(len(ch)):
        if("A"<=ch[i]<="F"):
            
            s=s+chr(int(baseb(DECIMAL(ch[i],10),8))+64)
            print(s)
        elif("G"<=ch[i]<="I"):
            s=s+str((ord(ch[i])-64))
            print(s)
        else:
            s=s+baseb(pgd(ord(ch[i])),16)
            print(s)
            
    return s

#01234567
def verif(x):
    j=0
    for i in range(len(x)):
        if("A"<=x[i]<="Z"):
            j=j+1
    return j==len(x)

def genere():
    cc=w.cc.text()
    n=w.nom.text()
    pr=w.pr.text()
    
    if(cc=="" or len(cc)!=8):
        QMessageBox.critical(w,'ERROR','Code is invalid')
    
    elif(n=="" or len(n)<4 or verif(n)==False):
        QMessageBox.critical(w,'ERROR','Last name is invalid')
    
    elif(pr=="" or len(pr)<4 or verif(pr)==False):
        QMessageBox.critical(w,'ERROR','Name is invalid')
    else:
        f=open('mdpass.dat','ab')
        e=dict()
        e["code"]=cc
        e["nom"]=n
        e["pr"]=pr
        if(w.rad1.isChecked()):
            e["type"]="Current "
        else:
            e["type"]="Savings"
        e['mdp']=mdp(n,pr)
        print(e)
        dump(e,f)
        f.close()
            
    


def afficher():
    f=open('mdpass.dat','rb')
    w.t.setRowCount(0)
    i=0
    test=True
    while test:
        try:
            e=load(f)
            print(e)
            w.t.insertRow(i)
            w.t.setItem(i,0,QTableWidgetItem(str(e['code'])))
            w.t.setItem(i,1,QTableWidgetItem(str(e['nom'])))
            w.t.setItem(i,2,QTableWidgetItem(str(e['pr'])))
            w.t.setItem(i,3,QTableWidgetItem(str(e['type'])))
            w.t.setItem(i,4,QTableWidgetItem(str(e['mdp'])))
            i=i+1
        except:
            test=False
    f.close()






w.bt1.clicked.connect(genere)
w.bt2.clicked.connect(afficher)
x.exec_()