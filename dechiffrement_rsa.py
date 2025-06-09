
# [[110, 71, 74, 103], [111, 105, 120, 103], [103, 112, 103, 67], [72, 100, 85, 81]]
d= 878699040824729336959163297596505832470328181635670468262021169150719833429
n= 2297357704302110809750625643728824203316031711887205300857786933950406436863
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

print(dechiffrement_cle("teste.txt",d,n))
