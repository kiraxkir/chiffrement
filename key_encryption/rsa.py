
from sympy import mod_inverse
from sympy import randprime
import random
import sys
import os
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
 
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop, "encryption_resultat/")
    os.makedirs(folder_path,exist_ok=True)
    with open(folder_path+"cle_chiffré.txt","w+") as f:

        for block in liste_message_chiffré :
            for valeur in block :

                f.write(f"{valeur} \n")
    with open(folder_path+"cle_privé.txt","w+") as c:

        c.write(f"{str((d,n))} le premier c est d et le deuxieme n")


    return " merci "