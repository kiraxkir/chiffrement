
import operator
import numpy as np
import secrets
import string
from sympy import mod_inverse
from sympy import randprime
import random
#ouverture du fichier a chiffrer


def generateur_mdp():
    letters = string.ascii_letters

    md=letters
    password = []
    for i in range(16) :
        password.append(secrets.choice(md))
    password=''.join(password)
    return password



with open(lien_fichier, "r", encoding="utf-8") as f:
    f.seek(0)
    contenu=f.read()
    padding=len(contenu)+(16-(len(contenu)%16))
    plain_texte=contenu.ljust(padding)

#user_message=input("bonjour !, veuillez entrer le message a chiffré ici ")
cle_user=generateur_mdp()
pas = 16




# matrice de rijndael pour la partie mix colomuns
matrice_de_rijndael=np.array([
[0x02,0x03,0x01,0x1],
[0x01,0x02,0x03,0x01],
[0x01,0x01,0x02,0x03],
[0x03,0x01,0x01,0x02]])
# tableau rcorne pour les 5 round 
r_corn_table=[[0x01,0x02,0x03,0x04],
[0x05,0x06,0x07,0x08],
[0x09,0xa,0xb,0xc],
[0xd,0xe,0xf,0x10],
[0x11,0x12,0x13,0x14]]
#la s box pour la partie subyte
s_box = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76], 
[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4,0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0], 
[0xb7,0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31,0x15], 
[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96,0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb,0x27, 0xb2, 0x75],
[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84], 
[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a,0xcb, 0xbe, 0x39, 0x4a,0x4a,0x58, 0xcf],
[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33,0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,0x9f, 0xa8], 
[0x51, 0xa3, 0x40, 0x8f, 0x92,0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2], 
[0xcd, 0xc0, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,0xc4, 0xac, 0x7e, 0x3d,0x64, 0x5d, 0x19, 0x73], 
[0x60 ,0x81, 0x4f, 0xdc, 0x22,0x2a, 0x90, 0x88,  0xee, 0xb8, 0x14, 0xde, 0x5e, 0x05, 0xdb], 
[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91,0x95, 0xe4, 0x79], 
[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8,0xdd, 0x74, 0x1f, 0x45,0xbd, 0x85, 0x8a], 
[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e], 
[0xe1, 0xf8, 0x98,0x11, 0x69, 0xd9, 0x8e, 0x94, 0x95,0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf], 
[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99,0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
print(len(s_box))

def RSA(cle_user):
    #f=open("teste.txt","w+")
    #generation des clé
    p=randprime(100,2000)
    q=randprime(100,3000)
    n=p*q
    Ø=(p-1)*(q-1)
    e=randprime(10,3000)
    d=mod_inverse(e,Ø)
    
    #clé pubique n et e clé publique c est d
    #message=input("veuillez entrer le message a transferer : ")
    liste_message=[m for m in cle_user]
    liste_ascii=[]
    for i in range(len(liste_message)):
        x=ord(liste_message[i])
        liste_ascii.append(x)
        x=0
    liste_message_chiffré=[]
    for i in range(len(liste_message)):
        y=liste_ascii[i]
        x=pow(y,e,n)
        x=str(x).zfill(7)
        #print(len(str(x)))
        liste_message_chiffré.append(x)
        y=0
        x=0

   # v=''.join(map(str,liste_message_chiffré[:]))
    #v=hex(v)
    dico={"cle_chiffré":liste_message_chiffré,"d": d , "n": n,"cle en claire":cle_user}

    return str(dico)
    



#variable message et cle: 

# calcul de la cle pour chaque round avec comme parametre une cle de 16 caractere et une matrice appellé round 5 tour
def round_cle(cle_user,round):
    import operator
    cle_liste=[format(ord(c),'02x') for c in cle_user]
    cle_round=[[],[],[],[]]
    temp=[]
    temp2=[]
    a=0
    b=4
    for i in range (4):
        temp=cle_liste[a:b]
        #cle_round[i]=temp
        
        for j in range(4):
            x=format(operator.xor(int(str(round[j]),16),int(temp[j],16)),'02x')
            temp2.append(x)
        cle_round[i]=temp2
        a+=4
        b+=4
        temp=[]
        temp2=[]
    return cle_round

#le resultat de cette boucle est cle round table qui repertorie les cle a utiliser dans les 5round 
# PADDING POUR LE REMPLISAGE A VOIRRRRRRRRR
#cette fonction ci desous est la creation du message pour les round appellé message_round  qui est une matrice 4*4
def message_round(message,cle_user):
    message=[format(ord(c),'02x') for c in message]
    cle_liste=[format(ord(c),'02x') for c in cle_user]
    liste_message_round=[[],[],[],[]]
    s=[]
    c=[]
    a=0
    b=4
    for i in range(4):
        c=cle_liste[a:b]
        s=message[a:b]
        a+=4
        b+=4
        for j in range(4):
             #xor du message et de la clé
            liste_message_round[i].append(format(operator.xor(int(s[j],16),int(c[j],16)),'x'))
            x=format(operator.xor(int(s[j],16),int(c[j],16)),'02x')
    #xor du message et de la clé
    #1 - subyte
    #cette boucle remplace les element de la s box
    for i in range(4):
        for j in range(4):
            temp=[c for c in liste_message_round[i][j]]
            if len(temp) != 2 :
                x=temp[0]
                temp[0]=0
                temp.append(x)
            x=int(str(temp[0]),16)
            y=int(str(temp[1]),16)
           # print(x,y)
        
            liste_message_round[i][j] = s_box[x][y]
    
    return liste_message_round[:]

tableau_message_general=[]



#print(tableau_message_general)
def codage_boucle(user_message,cle_user,matrice_de_rijndael,cle_round_table):
    message=message_round(user_message,cle_user)
    message_en_decimal= [[int(str(val), 16) for val in row] for row in message ]
    message_final=[[],[],[],[]]
     #mixcolomuns
    matrice_t=np.array(message_en_decimal).T

    final_matrice=np.dot(matrice_t, matrice_de_rijndael).tolist()

    for i in range(4):
        temps_key=cle_round_table[i]
        for j in range(4):
            val=format(
                operator.xor(
                    int(final_matrice[i][j]),
                    int(temps_key[i][j],16)
                    ),'02x')
            
            message_final[i].append(val)
    resultat= ''.join([''.join(row) for row in message_final])
    #resultat =str(message_final) 
    # le premier ''join c est pour la matrice et le deuxieme pour les liste 
  
    return resultat
resultat=open("resultat.txt","w+",encoding="utf-8")
cle_round_table=[[],[],[],[]]
   
for h in range(0,len(plain_texte),16):
    texte=plain_texte[h:h+16]
    for i in range(4):
        cle_round_table[i]=(round_cle(texte,r_corn_table[i]))

    rst=codage_boucle(texte,cle_user,matrice_de_rijndael,cle_round_table)
    resultat.write(rst)
    resultat.seek(0,2)

resultat.close()


#cle=round_cle(cle_user,round1)






