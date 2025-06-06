
a="iIlBxVMlejcUxVYt"
def RSA(cle_user):
    #generation des clé
    from sympy import mod_inverse
    from sympy import randprime
    import random

    p=randprime(10**2,10**5)

    q=randprime(10**2,10**5)
    n=p*q

    Ø=(p-1)*(q-1)

    e=randprime(10,200)

    d=mod_inverse(e,Ø)
    
    #clé pubique n et e clé publique c est d
    #message=input("veuillez entrer le message a transferer : ")
    liste_message=[m for m in cle_user]
    cle_chiffre=[]
    for i in range(len(liste_message)):
        x=ord(liste_message[i])
        cle_chiffre.append(x)
        x=0
    print(cle_chiffre[:])
    liste_message_chiffré=[]
    for i in range(16):
        y=cle_chiffre[i]
        x=pow(y,e,n)
        liste_message_chiffré.append(x)
        y=0
        x=0
    with open("clé_chiffré.bin","wb") as f:
        for j in liste_message_chiffré:
            f.write(bytes(j))
    


    return "merci"
    
print(RSA(a))