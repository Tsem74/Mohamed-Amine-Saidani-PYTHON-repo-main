from PyQt5.uic import*
from PyQt5.QtWidgets import*
from pickle import load,dump
from numpy import array
x=QApplication([])
w=loadUi('triage.ui')
w.show()
ch="une hirondelle ne fait pas le printemps"
def nb(ch):
    j=0
    for i in range(len(ch)):
        if(ch[i]==" "):
            j=j+1
    return j+1

def verif(ch):
    k=0
    for i in range(len(ch)):
        if("A"<=ch[i].upper()<="Z" or ch[i]==" "):
            k=k+1
    return k==len(ch)

def trier(ch):
    ch=ch+" "
    nbr=nb(ch)
    t=array([str]*nbr)
    
    for i in range(nbr):
        p=ch.find(' ')
        t[i]=ch[0:p]
        ch=ch[p+1:len(ch)]
    
    
        
    permut=True
    while permut:
        permut=False
        for j in range(nbr-1):
            if(len(t[j+1])<len(t[j])):
                aux=t[j]
                t[j]=t[j+1]
                t[j+1]=aux
                permut=False
    
    print(t)
    s=""
    for k in range(nbr):
        s=s+t[k]+" "
    return s

def afficher():
    f=open('trie.dat','rb')
    w.t.setRowCount(0)
    test=True
    i=0
    while test:
        try:
            e=load(f)
            w.t.insertRow(i)
            w.t.setItem(i,0,QTableWidgetItem(str(e['chaine'])))
            w.t.setItem(i,1,QTableWidgetItem(str(e['trie'])))
        except:
            test=False
    f.close()

def triage():
    ch=w.ch.text()
    if(ch=="" or nb(ch)>16 or not verif(ch)):
        QMessageBox.critical(w,'Error','Please enter 15 words')
    else:
        w.res.setText(trier(ch))
        f=open('trie.dat','ab')
        e=dict()
        e["chaine"]=ch
        e['trie']=trier(ch)
        dump(e,f)
        f.close()
        afficher()


w.bt1.clicked.connect(triage)
x.exec_()