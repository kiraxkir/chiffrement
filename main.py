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

def encryption (message,user_cle):
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

def decryptage(message,user_cle):
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

def cryptage(texte,cle):
    resultat=[]
    for i in texte : 
        x=i
        for j in range ( 5): 
            x=encryption(x,cle[j])
        resultat.append(x)
   

    with open("resultat.bin","wb") as f:
        for block in resultat:
            for ligne in block:
                f.write(bytes(ligne))

# start = time.perf_counter()

texte=plaintext.plaintext("exemple.txt")
cle=round_cle.cle()
print(texte)


resultat=[]
for i in texte : 
        x=i
        for j in range (5): 
            x=encryption(x,cle[j])
        resultat.append(x)
print(resultat)

decrype=[]

for i in resultat:
    y=i
    for j in range(1,6):
        y=decryptage(y,cle[-j])
    for a in range(4):
        for b in range(4):
            x=chr(y[a][b])
            decrype.append(x)       

print(''.join([c for c in decrype]))     

