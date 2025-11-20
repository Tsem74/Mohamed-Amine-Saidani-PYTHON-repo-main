from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import*
app=QApplication([])
w=loadUi("imei.ui")
w.show()

def verif(ch) :
    i=0
    while (i<len(ch) and ("A"<=ch[i].upper()<="Z" or ch[i]==" ") ):
        i=i+1
    return i==len(ch)


def ajouter():
    c=w.c.text()
    p=w.p.text()
    a=w.a.text()
    cb=w.cb.currentText()
    
    if (c=="" or len(c)!=15 ):
        QMessageBox.critical(w,"Error","IMEI code must have 15 characters")
        w.c.clear()
    elif p=="" or not verif(p) :
        QMessageBox.critical(w,"Error","Please enter owner's full name")
        w.p.clear()
    elif a=="" or int(a)<2015:
        QMessageBox.critical(w,"Error","Year must be higher than 2015")
        w.a.clear()
    elif cb=="":
        QMessageBox.critical(w,"Error","Please choose a brand")
        
    elif w.four.isChecked==False and w.five.isChecked==False:
        QMessageBox.critical(w,"Error","Check a Network")
    else:
        f=open("appareil.dat","ab")
        e=dict()
        
        e["code"]=c
        e["pr"]=p
        e["a"]=a
        e["m"]=cb
        if w.four.isChecked():
            e["cat"]="4G"
        else:
            e["cat"]="5G"
        dump(e,f)
        QMessageBox.information(w,"Addition","Device added successfully")
        f.close()
        
def affiche():
    f=open("appareil.dat","rb")
    
    w.t.setRowCount(0)
    
    
    test=True
    i=0
    while test==True:
        try:
            e=load(f)
            print(e)
            print("gjkgjk")
            w.t.insertRow(i)
            w.t.setItem(i,0,QTableWidgetItem(str(e["code"])))
            w.t.setItem(i,1,QTableWidgetItem(str(e["pr"])))
            w.t.setItem(i,2,QTableWidgetItem(str(e["a"])))
            w.t.setItem(i,3,QTableWidgetItem(str(e["m"])))
            w.t.setItem(i,4,QTableWidgetItem(str(e["cat"])))
            i=i+1
        except:
            test=False
    f.close()



"""def valid(c):
    s=0
    
    for i in range(len(c)):
        if i%2==0:
            s=s+int(c[i])
            print(s)
        else:
            
            x=int(c[i])*2
            if(x>=10):
                ch=str(x)
                s=s+int(ch[0])+int(ch[1])
    
            
   
    if s%10==0:
        return True
    else:
        return False"""

def valid(c):
    s=""
    v=0
   
    for i in range (0,len(c)):
        if i%2==0:
            s=s+c[i]
        else:
            p=int(c[i])*2
            if (p>9):
                x=str(p)
                
                s=s+str(int(x[0])+int(x[1]))
            else:
                #MATENSACH LCAS OU P EST UN SEULE CHIFFRE: 30MINS WINTI TLAWEJ 3LECH GHALTA!!!!!!!!
                s=s+str(p)
    

    for i in range(0,len(s)):
        
        v=v+int(s[i])
    
   
    if v%10==0:
        return True
    else:
        return False


def affiche2():
    f=open("appareil.dat","rb")
    f2=open("blockage.txt","a")
    
    test=True
    while test:
        try:
            e=load(f)
            
            if e["m"]=="samsung" and not valid(str(e["code"])):
                f2.write(str(e["code"])+e["pr"]+"\n")
                w.l.addItem(e["code"]+" "+e["pr"])
        except:
            test=False
    
    f.close()
    f2.close()

#354365039281174
#100000000001111

w.bt1.clicked.connect(ajouter)
w.bt2.clicked.connect(affiche)
w.bt3.clicked.connect(affiche2)

app.exec_()