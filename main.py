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



# start = time.perf_counter()

texte=plaintext.plaintext("exemple.txt")
cle=[[[88, 107, 119, 110], [111, 112, 97, 126], [100, 75, 65, 105], [102, 82, 112, 66]], [[92, 111, 115, 98], [107, 116, 101, 114], [96, 79, 69, 101], [98, 86, 116, 78]], [[80, 99, 127, 102], [103, 120, 105, 118], [108, 67, 73, 97], [110, 90, 120, 74]], [[84, 103, 123, 122], [99, 124, 109, 106], [104, 71, 77, 125], [106, 94, 124, 86]], [[72, 123, 103, 126], [127, 96, 113, 110], [116, 91, 81, 121], [118, 66, 96, 82]]]

resultat=[]
for i in texte :
    for j in range (5):
        i=encryption(i,cle[j])
    resultat.append(i)

print(resultat)
print("\n")
print("\n")
print("\n")
print("-------------------------------------------------------decrypatge------------------------------------------------------------")

resultat2=[]
for i in resultat : 
    for j in range (1,5) :
        i=decryptage(i,cle[-j])
    resultat2.append(i)

print(resultat2)
print("-"*40)
print(texte)