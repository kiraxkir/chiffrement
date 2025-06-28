
import os

from datetime import datetime

#creation du dossier pour le resultat
# os.rename(r"C:\Users\HP\Desktop\encryption_project\kira","gui")

import sys
sys.path.append("module")
sys.path.append("key_encryption")

import os
from key_encryption.invrsa import dechiffrement_cle
from module import plaintext    
from module import subyte
from module import mixcolumn
from module import shiftrows              # les different package garce a type NUL > __init__.py  
from module import Addroundkey
import numpy as np
import time
from pprint import pprint
from module import round_cle
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
    key=dechiffrement_cle(lien_cle,lien_private)
    cle=round_cle.invcle(key)
    start = time.perf_counter()
    texte=plaintext.invplaintext(lien_fichier) # est un fichier binaire invisible a l oeil nu
  
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



    now=datetime.now()
    date_str = now.strftime("%d.%m.%y-%Hh%M")
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    desktop= os.path.join(desktop,"dechiffrement")
    os.makedirs(desktop,exist_ok=True)
    filename="decryption_result "+date_str
    folder_path = os.path.join(desktop,filename)

    os.makedirs(folder_path,exist_ok=True)

    name_file= os.path.join(folder_path,"message_déchiffré.txt")
    with open(name_file,"w+") as f:
        f.write(resultat)

    fin = time.perf_counter()

    print(f"le dechiffrement a pris {fin - start:.4f} second")
    return "merci"

# [[90, 87, 122, 89], [72, 103, 101, 85], [79, 81, 84, 76], [102, 116, 98, 85]]
