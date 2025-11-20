from numpy import array
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import load,dump
t=array([[int]*20]*10)
x=QApplication([])
w=loadUi("bac.ui")
w.show()
w.setWindowTitle('bac-Graphique')






"""def saisir():
    c=input("saisir un code")
    while len(c)!=13:
        c=input("saisir un code")
    return c"""

def prem(n):
    k=2
    while k<=n//2 and n%k!=0:
        k=k+1
    return k>n//2

def binaire(x):
    b=""
    while x!=0:
        if x%2<=9:
            
            b=str(x%2)+b
        else:
            b=str((x%2)+55)+ch
            
        x=x//2
        
    return b

def zero(b):
    k=0
    for i in range(len(b)):
        if b[i]=="0":
            k=k+1
    return k

def verif(c):
    if prem(int(c[0:3])) and (zero(binaire(int(c[3:8])))>8) and int(c[8:])%int(c[:3])==0:
        print("true")
        return True
    else:
        print("false")
        return False
        
def exist(c):
    f=open("source.txt","r")
    ch=f.readline()
    if ch[:13]!=c and len(ch)!=0:
        ch=f.readline()
    elif ch[:13]==c:
        return True
    else:
        return False
    
    f.close()
   

def verifcode():
    c=w.c.text()
    i=0
    w.t.setColumnCount(1)
    if c=="" or len(c)!=13:
        QMessageBox.critical(w,"erreur","saisir un code de 13 chiffres ")
        w.c.clear()
    elif not verif(c):
        QMessageBox.warning(w,"Erreur","Code Invalide")
    elif verif(c) and  exist(c)==False:
        QMessageBox.warning(w,"Erreur","Code Deja Utilise")
    else:
        w.t.insertRow(i)
        w.t.setItem(i,0,QTableWidgetItem(str(c)))
        i=i+1
        QMessageBox.information(w,"Info","Code Valide")
       
def affiche():
    f=open("source.txt","r")
    ch=f.readline()
    while ch!="":
        w.l.addItem(ch)
        ch=f.readline()

    f.close
def reset():
    w.c.clear()
    w.l.clear()
    w.t.setRowCount(0)

w.bt1.clicked.connect(verifcode)
w.bt2.clicked.connect(affiche)
w.bt3.clicked.connect(reset)
"""#test code: 2114512367731"""
x.exec_()