import generateur_mdp

import numpy as np

rcorn=[[0x01,0x02,0x03,0x04],
[0x05,0x06,0x07,0x08],
[0x09,0xa,0xb,0xc],
[0xd,0xe,0xf,0x10],
[0x11,0x12,0x13,0x14]]
user_cle=generateur_mdp.generateur_mdp()

def round_cle(cle_user,round):
    resultat=[]
    user_cle=[c for c in cle_user]
    round=[c for c in round]
    for i in range(4):
        tmp=[]
        for j in range(4):
            a=( user_cle[i][j]  ^  round[j] )
            tmp.append(a)
        resultat.append(tmp)
    return resultat


def cle():
    cle=[]
    for i in range(5) :
        x=round_cle(user_cle,rcorn[i])
        cle.append(x)
    return cle

