
def dechiffrement_cle(lien_fichier,d,n) :
    tmp=[]
    tmp2=[]

    resultat=[]
    with open(lien_fichier,"r")  as f : 
        for i in f :
            a=int(i)
            x=pow(a,d,n)
            tmp.append(x)
        for j in range(0,16,4) :
            tmp1=tmp[j:j+4]
            resultat.append(tmp1)
    return resultat
