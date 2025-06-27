import sys

sys.path.append("module")
sys.path.append("key_encryption")
import os
import plaintext

import plaintext
import subyte
import mixcolumn
import shiftrows
import Addroundkey
from copy import copy
import time
from pprint import pprint
from rsa import folder_path
    
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

def cryptage(lien_fichier,name):


    import round_cle


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
    
    os.rename(folder_path, folder_path+'by'+name)
    end = time.perf_counter()
    print(f"le chiffrement a pris {end - start:.4f} second")

    return "merci"

