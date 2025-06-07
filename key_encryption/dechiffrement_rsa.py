import numpy as np

d=1709464481935456015182295955405792218402789668934060774240941294911291649359
n=2288942996654094894633600768051570153956565511181792925980237303018337073393
tmp=[]
tmp2=[]

resultat=[]
with open("teste.txt","r")  as f : 
    for i in f :
        a=int(i)
        x=pow(a,d,n)
        tmp.append(x)
    for j in range(0,16,4) :
        tmp1=tmp[j:j+4]
        resultat.append(tmp1)

print(resultat)
