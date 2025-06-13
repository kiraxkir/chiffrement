from sympy import mod_inverse
from sympy import randprime

import generateur_mdp
password=generateur_mdp.generateur_mdp()

def RSA(cle_user):
    #f=open("teste.txt","w+")
    #generation des clé
    p=randprime(100,2000)
    q=randprime(100,3000)
    n=p*q
    Ø=(p-1)*(q-1)
    e=randprime(10,3000)
    d=mod_inverse(e,Ø)
    
    #clé pubique n et e clé publique c est d
    #message=input("veuillez entrer le message a transferer : ")
    liste_message=[m for m in cle_user]
    liste_ascii=[]
    for i in range(len(liste_message)):
        x=ord(liste_message[i])
        liste_ascii.append(x)
        x=0
    liste_message_chiffré=[]
    for i in range(len(liste_message)):
        y=liste_ascii[i]
        x=pow(y,e,n)
        x=str(x).zfill(7)
        #print(len(str(x)))
        liste_message_chiffré.append(x)
        y=0
        x=0

   # v=''.join(map(str,liste_message_chiffré[:]))
    #v=hex(v)
    dico={"cle_chiffré":liste_message_chiffré,"d": d , "n": n,"cle en claire":cle_user}

    return str(dico)

cle_de_chiffrement=open("cle_chiffré.txt","w",encoding="utf-8")
cle_de_chiffrement.write(RSA(password))
cle_de_chiffrement.close()