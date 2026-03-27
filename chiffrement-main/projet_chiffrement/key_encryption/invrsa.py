def dechiffrement_cle(lien_cle,lien_dn) :
    
    l=[]
    with open(lien_dn,"r") as f:
        for i in f :
            
    
            l.append(int(i))
    d=l[0]
    n=l[1]

    resultat=[]
    with open(lien_cle,"r")  as f : 
        tmp=[]
        for block in f:
            y=block
            y=int(y)
            x=pow(y,d,n)
            tmp.append(x)
            y=0
            x=0
    for j in range(0,16,4) :
            tmp1=tmp[j:j+4]
            resultat.append(tmp1)
    
    return resultat

