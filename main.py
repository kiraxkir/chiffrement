
import plaintext
import subyte
import mixcolumn
import shiftrows
import Addroundkey
import numpy as np
import time
from pprint import pprint
import round_cle
from copy import copy
import json


def chiffrement (message,user_cle):
    message=[c for c in message]

    cle=[c for c in user_cle ]
    #subyte part
    m1=subyte.subyte(message,user_cle)
    

    #shiftrow part 
    m2=shiftrows.shiftrows(m1)

    #mix columns
    m3=mixcolumn.mixcolumn(m2)
    #addround key
    m4=Addroundkey.addroundkey(m3,cle)
    return m4

def dechiffrement (message,user_cle):
    message=[c for c in message]
    cle=[c for c in user_cle ]
    #add round key decrypt
    m1=Addroundkey.invaddroundkey(message,cle)
    #invmix colomuns
    m2=mixcolumn.invMixColumns(m1)
    #inv shiftrows
    m3=shiftrows.invshiftrows(m2)
    #inverse subyte
    m4=subyte.invsubyte(m3,cle)
    return m4
cle=[[[82, 79, 66, 96], [75, 80, 108, 87], [103, 110, 76, 69], [112, 85, 108, 71]], [[86, 75, 70, 108], [79, 84, 104, 91], [99, 106, 72, 73], [116, 81, 104, 75]], [[90, 71, 74, 104], [67, 88, 100, 95], [111, 102, 68, 77], [120, 93, 100, 79]], [[94, 67, 78, 116], [71, 92, 96, 67], [107, 98, 64, 81], [124, 89, 96, 83]], [[66, 95, 82, 112], [91, 64, 124, 71], [119, 126, 92, 85], [96, 69, 124, 87]]]

def cryptage(lien_fichier,cle):
    start = time.perf_counter()
    texte=plaintext.plaintext(lien_fichier)
    

    resultat=[]
    for i in texte : 
        x=i
        for j in range ( 5): 
            x=chiffrement(x,cle[j])
        resultat.append(x)
   

    with open("resultat_chiffré.bin","wb") as f:
        for block in resultat:
            for ligne in block:
                f.write(bytes(ligne))
    end = time.perf_counter()
    print(f"le chiffrement a pris {end - start:.4f} second")

    return "merci"


def decryptage(lien_fichier,cle):

    start = time.perf_counter()

    texte=plaintext.invplaintext(lien_fichier) # est un fichier binaire invisible a l oeil nu
    cle=[c for c in cle]
    decrype=[]
    resultat= texte

    for i in resultat:
        y=i
        for j in range(1,6):

            y=dechiffrement(y,cle[-j])

        for a in range(4):

            for b in range(4):

                x=chr(y[a][b])

                decrype.append(x)    
    r_f =''.join([c for c in decrype]) # resultat final
    print(r_f)
    with open("message_déchiffré.txt","w+") as f:
        f.write(str(r_f))
    fin = time.perf_counter()

    print(f"le dechiffrement a pris {fin - start:.4f} second")
    return "merci"

print(decryptage("resultat_chiffré.bin",cle))