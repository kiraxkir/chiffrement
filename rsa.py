
import sys
sys.path.append('C:/Users/HP/Desktop/fac/aes\chiffrement_aes')
import generateur_mdp
import generateur_mdp
from sympy import mod_inverse
from sympy import randprime
import random

def RSA():
    #generation des clé
  
    cle=generateur_mdp.key()
    print(cle)
    p=randprime(10**20,10**38) # j ai choisi arbitrairement les valeur de p et q 

    q=randprime(10**20,10**38)

    n=p*q

    Ø=(p-1)*(q-1)

    e=randprime(10**14,10**20)

    d=mod_inverse(e,Ø)
    
    #clé pubique n et e clé privé c est d
    print("d=",d)
    print("n=",n)
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

    with open("teste.txt","w+") as f:
        for block in liste_message_chiffré :
            for valeur in block :
                f.write(f"{valeur} \n")
    


    return " merci "
print(RSA())