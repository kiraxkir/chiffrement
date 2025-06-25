import sys
sys.path.append("module")
sys.path.append("key_encryption")
import invrsa
import os
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
import shutil # pour le deplacement du dossier après chiffrement 
#from generateur_mdp import fichier


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

def decryptage(lien_fichier,lien_cle,lien_private):
    start = time.perf_counter()
    key=invrsa.dechiffrement_cle(lien_cle,lien_private)
    cle=round_cle.invcle(key)
    start = time.perf_counter()
    texte=plaintext.invplaintext(lien_fichier) # est un fichier binaire invisible a l oeil nu
  
    decrype=[]


    for i in texte:
        y=i
        for j in range(1,6):
            print(y)

            y=dechiffrement(y,cle[-j])

        for a in range(4):

            for b in range(4):

                x=chr(y[a][b])

                decrype.append(x)    
    resultat =''.join([c for c in decrype]) # resultat final
    print(resultat)
    with open("message_déchiffré.txt","w+") as f:
        f.write(resultat)

    fin = time.perf_counter()

    print(f"le dechiffrement a pris {fin - start:.4f} second")
    return "merci"

# [[90, 87, 122, 89], [72, 103, 101, 85], [79, 81, 84, 76], [102, 116, 98, 85]]

print(decryptage("encrypted_file.bin","key.txt","private.txt"))