import sys
sys.path.append("module")
sys.path.append("key_encryption")
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
from rsa import*
import shutil # pour le deplacement du dossier après chiffrement 



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
    filename=os.path.join(folder_path,"encrypted_file.bin")
    with open(filename,"wb") as f:
        for block in resultat:
            for ligne in block:
                f.write(bytes(ligne))
    
    
    end = time.perf_counter()
    print(f"le chiffrement a pris {end - start:.4f} second")

    return "merci"

# cle=[[74, 117, 106, 115], [106, 105, 111, 107], [69, 121, 112, 117], [74, 101, 112, 112]]

# round_cle=[[[75, 119, 105, 119], [107, 107, 108, 111], [68, 123, 115, 113], [75, 103, 115, 116]], [[79, 115, 109, 123], [111, 111, 104, 99], [64, 127, 119, 125], [79, 99, 119, 120]], [[67, 127, 97, 127], [99, 99, 100, 103], [76, 115, 123, 121], [67, 111, 123, 124]], [[71, 123, 101, 99], [103, 103, 96, 123], [72, 119, 127, 101], [71, 107, 127, 96]], [[91, 103, 121, 103], [123, 123, 124, 127], [84, 107, 99, 97], [91, 119, 99, 100]]]

# texte=[[76, 97, 32, 112], [111, 115, 115, 105], [98, 105, 108, 105], [116, 233, 32, 100]], [[101, 32, 102, 97], [105, 114, 101, 32], [102, 111, 114, 116], [117, 110, 101, 32]]

#print(cryptage("exemple.txt"))