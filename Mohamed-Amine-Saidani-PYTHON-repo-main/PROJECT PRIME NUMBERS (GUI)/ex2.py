from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import load,dump
x=QApplication([])
w=loadUi("ex2.ui")
w.show()
w.setWindowTitle('TP2-Graphique')

def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

def generer():
    f1=open("source.txt","r")
    f2=open("result.dat","wb")
    e=dict()
    ch1=f1.readline()
    while ch1!="":
        
        a=int(ch1[:ch1.find(" ")])
        
        b=int(ch1[ch1.find(" "):])
        
        if ((fact(a)*fact(b))%(a+b))==a or ((fact(a)*fact(b))%(a+b))==b:
            e["a"]=str(a)
            e["b"]=str(b)
            e["a+b"]=str(a+b)
            dump(e,f2) 
            
        print(e)
        ch1=f1.readline()
              
            
    
    f1.close()
    f2.close()

def affich():
    f1=open("source.txt","r")
    ch=f1.readline()
    while ch!="":
        w.src.addItem(ch)
        ch=f1.readline()
    
    f1.close()
    
    f2=open("result.dat","rb")
    test=True
    i=0
    w.res.setColumnCount(3)
    while test==True:
       try:
           ch2=load(f2)
           w.res.insertRow(i)
           w.res.setItem(i,0,QTableWidgetItem(str(ch2["a"])))
           w.res.setItem(i,1,QTableWidgetItem(str(ch2["b"])))
           w.res.setItem(i,2,QTableWidgetItem(str(ch2["a+b"])))
           i=i+1
       except:
            test=False
        
    f2.close() 
def clear():
    w.src.clear()
    w.res.setRowCount(0)

     
        
w.bt1.clicked.connect(generer)
w.bt2.clicked.connect(affich)
w.bt3.clicked.connect(clear)
x.exec_()