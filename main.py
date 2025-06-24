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
from generateur_mdp import fichier 

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

def cryptage(lien_fichier):
    cle=round_cle.cle()
    start = time.perf_counter()
    texte=plaintext.plaintext(lien_fichier)
    

    resultat=[]
    for i in texte : 
        x=i
        for j in range ( 5): 
            x=chiffrement(x,cle[j])
        resultat.append(x)
    
        # "encryption_resultat/
    filename=os.path.join(fichier,"encrypted_file.bin")
    with open(filename,"wb") as f:
        for block in resultat:
            for ligne in block:
                f.write(bytes(ligne))
    
    
    end = time.perf_counter()
    print(f"le chiffrement a pris {end - start:.4f} second")

    return "merci"



def decryptage(lien_fichier,lien_cle,lien_private):
    start = time.perf_counter()
    cle=invrsa.dechiffrement_cle(lien_cle,lien_private)
    cle=round_cle.invcle(cle)
    start = time.perf_counter()
    texte=plaintext.invplaintext(lien_fichier) # est un fichier binaire invisible a l oeil nu
    print(np.shape(np.array(texte)))
    decrype=[]


    for i in texte:
        y=i
        for j in range(1,6):

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




print(decryptage("encrypted_file.bin","key.txt","private.txt"))
