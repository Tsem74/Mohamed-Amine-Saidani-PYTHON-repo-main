from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import*
from numpy import array
x=QApplication([])
w=loadUi("mdp.ui")
w.show()
def verif(ch):
   j=0
   for i in range(len(ch)):
       if '0'<=ch[i]<='9':
           j=j+1
   return j==len(ch)

def verif2(ch):
   k=0
   while k<len(ch) and 'A'<=ch[k]<='Z':
       
       k=k+1
   return k==len(ch)

def prem(x):
    i=2
    while i<=x//2 and x%i!=0:
        i=i+1
    return i>x//2
        

def div(n):
    maxi=0
    for i in range(1,n+1):
        if prem(i) and n%i==0 and i>maxi:
            maxi=i
    return maxi

def puis(x,y):
    p=1
    for i in range (y):
        p=p*x
    return p

def base10(x,b):
    s=0
    for i in range (len(x)):
        if x[i]<='9':
            s=s+int(x[i])*(puis(b,len(x)-i-1))
        else:
            s=s+int(ord(x[i])-55)*puis(b,len(x)-i-1)
    return s

def baseb(n,b):
    ch=""
    while n!=0:
        if n%b<=9:
            ch=str(n%b)+ch
        else:
            ch=chr((n%b)+55)+ch
        n=n//b
    return ch

def generer():
    c=w.c.text()
    n=w.n.text()
    p=w.p.text()
    e=dict()
    f=open('mdp.dat','wb')
    if not verif(c) or len(c)!=8:
        QMessageBox.warning(w,'erreur','code saisir 8 chiffre')
        w.c.clear()
    elif not verif2(n) or len(n)<4:
        QMessageBox.warning(w,'erreur','code nom saisir 4 lettre alpha majus')
        w.n.clear()
    elif not verif2(p) or len(p)<4:
        QMessageBox.warning(w,'erreur','code prenom saisir 4 lettre alpha majus ')
        w.p.clear()
    else:
        ch=n[0:4]+p[0:4]
        
        k=""
        for i in range (len(ch)):
            if 'A'<=ch[i]<='F':
                d=baseb(base10(ch[i],10),8)
                
                k=k+chr(int(d)+64)
            elif 'G'<=ch[i]<='I':
                k=k+str(ord(ch[i])-64)
                print(k)
            elif 'J'<=ch[i]<='Z':
                k=k+baseb(div(ord(ch[i])),16)
        print(k)
        e['code']=c
        e['nom']=n
        e['prénom']=p
        if w.r1.isChecked():
            e["compte"]='courant'
        elif w.r2.isChecked():
            e["compte"]='epargne'
        e['mdp']=k
        
        print(e)
        
        dump(e,f)
    f.close()   

def afficher():
    f=open('mdp.dat','rb')
    
    test=True
    
    while test==True:
        try:
            ch=load(f)
            i=0
            w.t.setColumnCount(5)
            w.t.insertRow(i)
            
            w.t.setItem(i,0,QTableWidgetItem(str(ch['code'])))
            w.t.setItem(i,1,QTableWidgetItem(str(ch['nom'])))
            w.t.setItem(i,2,QTableWidgetItem(str(ch['prénom'])))
            w.t.setItem(i,3,QTableWidgetItem(str(ch['compte'])))
            w.t.setItem(i,4,QTableWidgetItem(str(ch['mdp'])))
            
            i=i+1
        except:
            test=False
    
    f.close()
w.bt1.clicked.connect(generer)
w.bt2.clicked.connect(afficher)
x.exec_()


