import plaintext
import subyte
import mixcolumn
import shiftrows
import Addroundkey
import numpy as np
import time
from pprint import pprint
import round_cle

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



start = time.perf_counter()

texte=plaintext.plaintext("exemple.txt")
cle=round_cle.cle()

for i in texte :
    rs=i
    for j in range(5) : 
        rs=encryption(rs,cle[j])
        print(rs)
