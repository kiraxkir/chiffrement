
# la fonction addroundkey fais un xor ente le message et la cle 

def addroundkey(message,key):
    tmp = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            tmp[i][j]=message[i][j] ^ key[i][j]
    return tmp

def invaddroundkey(message,key):
    tmp = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
             tmp[i][j]=message[i][j] ^ key[i][j]
    return tmp

