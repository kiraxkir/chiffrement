
from sympy import mod_inverse
from sympy import randprime
import random
import sys
import os

from datetime import datetime


now=datetime.now()
date_str = now.strftime("%d_%m_%y-%Hh%M")
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
desktop= os.path.join(desktop,"chiffrement_resultat")
os.makedirs(desktop,exist_ok=True)
filename="encryption_result "+date_str
folder_path = os.path.join(desktop,filename)
# j ai l ai executer dans round cle, je ne sais pas pourquoi aussi 


def RSA(cle):
    

    #generation des clé
    p=randprime(10**20,10**38) # j ai choisi arbitrairement les valeur de p et q 

    q=randprime(10**20,10**38)

    n=p*q

    Ø=(p-1)*(q-1)

    e=randprime(10**14,10**20)

    d=mod_inverse(e,Ø)
    
    #clé pubique n et e clé privé c est d
    liste_message_chiffré=[]
    for block in cle:
        tmp=[]
        for ligne in block: 
            y=ligne
            x=pow(y,e,n)
            tmp.append(x)
            y=0
            x=0
        liste_message_chiffré.append(tmp)
       
   # creation _ du fichier de sauvegrade


    os.makedirs(folder_path,exist_ok=True)

 

    path=os.path.join(folder_path,"key.txt")

    with open(path,"w+") as f:
        for block in liste_message_chiffré :
            for valeur in block :

                f.write(f"{valeur} \n")
    path=os.path.join(folder_path,"private.txt")

    with open(path,"w+") as c:
        c.write(f"{d}\n")
        c.write(f"{n}")   
    print("RSA !!!!!!!!!!!!!!!!!!!!!!")
    return 'rsa '

