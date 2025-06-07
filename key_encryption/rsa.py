


key=[[101, 104, 98, 118], [121, 103, 117, 32], [98, 106, 101, 122], [110, 44, 59, 102]]
def RSA(cle):
    #generation des clé

    from sympy import mod_inverse
    from sympy import randprime
    import random

    p=randprime(10**20,10**38) # j ai choisi arbitrairement les valeur de p et q 

    q=randprime(10**20,10**38)

    n=p*q

    Ø=(p-1)*(q-1)

    e=randprime(10**14,10**20)

    d=mod_inverse(e,Ø)
    
    #clé pubique n et e clé privé c est d
    print(d)
    print(n)
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
print(RSA(key))