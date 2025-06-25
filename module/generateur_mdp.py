import sys
sys.path.append("key_encryption")

import secrets
import string
import rsa
# genere une liste de 4*4 de la cle
from datetime import datetime
def key():
    letters = string.ascii_letters

    md=letters
    password = []
    for i in range(16) :
        password.append(secrets.choice(md))
    password=''.join(password)
    mdp=[]
    a=[]

    for i in range(0,16,4):
        a=password[i:i+4]
        mdp.append(a)
        a=[ord(c) for c in password]
        mdp = [a[i:i+4] for i in range(0, 16, 4)]
    print(mdp)
    print("ggenereateur de mdp !!!!!!!!!!")
    return mdp
