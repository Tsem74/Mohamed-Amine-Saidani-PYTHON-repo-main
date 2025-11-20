from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import load,dump
x=QApplication([])
w=loadUi('sujetA.ui')
w.show()
code="4719512002889"

def verif(x):
    j=0
    for i in range (len(x)):
        if("A"<=x[i].upper()<="Z" or x[i]==" "):
            j=j+1
    return j

def ajouter():
    code=w.code.text()
    lib=w.lib.text()
    qu=w.qu.text()
    typ=w.typ.currentText()
    
    if(len(code)!=13 or code.isdecimal()==False):
        QMessageBox.critical(w,'Erreur','Code doit etre 13 chiffres')
    
    elif(lib=="" or not verif(lib)):
        QMessageBox.critical(w,'Erreur','Libelle doit etre forme par des lettres alpha et espaces')
    
    elif(len(qu)==0 or int(qu)<1):
        QMessageBox.critical(w,'Erreur','Quantite doit etre positive')
        
    elif(typ==""):
        QMessageBox.critical(w,'Erreur','Veuiller choisir un type')
    
    elif(w.rad1.isChecked()==False and w.rad2.isChecked()==False ):
        QMessageBox.critical(w,'Erreur','Vous devez cocher la nature')
    
    else:
        f=open('produit.dat','ab')
        e=dict()
        e["code"]=code
        e["libelle"]=lib
        e["quantite"]=qu
        e["type"]=typ
        if(w.rad1.isChecked()):
            e["nature"]="local"
        else:
            e["nature"]="importe"
        print(e)
        dump(e,f)
        QMessageBox.information(w,"Ajout","Produit ajoute avec sucess")
        
        f.close()
        
    
    
    


def afficher():
    f=open('produit.dat','rb')
    w.t.setRowCount(0)
    r=0
    test=True
    while test:
        try:
            e=load(f)
            print(e)
            w.t.insertRow(r)
            w.t.setItem(r,0,QTableWidgetItem(str(e["code"])))
            w.t.setItem(r,1,QTableWidgetItem(str(e["libelle"])))
            w.t.setItem(r,2,QTableWidgetItem(str(e["quantite"])))
            w.t.setItem(r,3,QTableWidgetItem(str(e["type"])))
            w.t.setItem(r,4,QTableWidgetItem(str(e["nature"])))
            r=r+1
        except:
            test=False
    f.close()
            
def imit(c):
    
    cc=c[-1]
    print(cc)
    s=0
    for i in range(len(c)-1):
        if(i%2==0):
            s=s+int(c[i])
        else:
            s=s+int(c[i])*3
    
    
    return 10-(s%10)==cc
            
    
    
    


def imitation():
    f=open('produit.dat','rb')
    f2=open('imitation.txt','w')
    
    test=True
    while test:
        try:
            
            e=load(f)
            print(e["code"]+" "+e["libelle"])
            
            #Ya 7marr imitation lezemha traj3 false 
            if(imit(e["code"])==False):
                var=e["code"]+" "+e["libelle"]
                print(var)
                f2.write(var+"\n")
        
        except:
            test=False
    f.close()
    f2.close()
    
    f3=open('imitation.txt','r')
    ch=f3.readline()
    print(ch)
    while ch!="":
        w.l.addItem(str(ch))
        ch=f3.readline()
    
    
    f3.close()
            
        




w.bt1.clicked.connect(ajouter)
w.bt2.clicked.connect(afficher)
w.bt3.clicked.connect(imitation)

x.exec_()


