
#import operator
from module.base import s_box, sbox
import copy

def subyte(m,cle_user):
    message=[c for c in m]
    cle_liste=[c for c in cle_user]
    for i in range(4) :
        for j in range( 4):
            temp=message[i][j]
            if temp > 255 :
                temp=32
     
            message[i][j] = sbox[temp]

    liste_subyte=[]
    for i in range(4):
        me=message[i]
        cl=cle_liste[i]
        temp =[]
        for j in range(4):
            #xor du message et de la clé
            xor= int(me[j]) ^ int(cl[j])
            temp.append(xor)
        liste_subyte.append(temp)
    return liste_subyte

    
def invsubyte(m,cle_user):
    message=[c for c in m]
    cle_liste=[c for c in cle_user] 
    liste_subyte=[] 
    for i in range(4):
        me=message[i]
        cl=cle_liste[i]
        temp =[]
        for j in range(4):
            #xor du message et de la clé
            xor= int(me[j]) ^ int(cl[j])
            temp.append(xor)
        liste_subyte.append(temp)
    for i in range(4):
        for j in range(4):
            temp=liste_subyte[i][j]
            liste_subyte[i][j]=sbox.index(temp)   

    return liste_subyte    

