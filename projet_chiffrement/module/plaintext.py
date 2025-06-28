import os
import numpy as np
def nettoyer_texte(contenu):
    texte=contenu
    remplacements = {
        
        '‘': "'", '’': "'",
        '“': '"', '”': '"',
        '«': '"', '»': '"',
        '–': '-', '—': '-',
        '−': '-',"’" : "'",
        '\n':'', 
        '\u00A0': ' ', '\u2009': ' ', '\u200A': ' ', '\u200B': ''
    }
    for ancien, nouveau in remplacements.items():
        texte= texte.replace(ancien, nouveau)
    return texte

def plaintext(lien_fichier):

    if not os.path.isfile(str(lien_fichier)):
      
      raise ValueError("the file " + str(lien_fichier) + " does not exist")
    
    else: 

        tabMess=[]

        with open(lien_fichier, "r", encoding="utf-8") as f:
            f.seek(0)

            contenu=f.read()



            padding=(len(contenu))+(16-(len(contenu)%16))%16
      

            plain_texte=contenu.ljust(padding)
           

    resultat=[]
    for i in range(0,len(plain_texte),16):
        temp=[]
        tmp2=[]
        x=[ord(x) for x in plain_texte[i:i+16]]
        for i in range(0,16,4):
            temp=x[i:i+4]
            tmp2.append(temp)
        resultat.append(tmp2)
    return resultat
#tabMess sera utiliser dans message round



def invplaintext(lien_fichier) :


    with open(lien_fichier,"rb") as f:
        bit=f.read()
        l_c=list(bit) # liste chiffre
    liste_chiffre=[]
    resultat=[]
    for i in range(0,len(l_c),16):
        liste_chiffre.append(l_c[i:i+16])
    for i in liste_chiffre :
        tmp1=[]
        tmp2=[]
        for j in range(0,16,4) :
            tmp1=i[j:j+4]
            tmp2.append(tmp1)
        resultat.append(tmp2)
    return resultat

