
# la fonction addroundkey fais un xor ente le message et la cle 

def addroundkey(message,key):
    tmp = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            tmp[i][j]=message[i][j] ^ key[i][j]
    return tmp

def invaddroundkey(message,key):
   # tmp = [[0 for x in range(4)] for x in range(4)]
    tmp=[]
    for i in range(4):
        for j in range(4):
        #    print(message[i][j])
            tmp.append(message[i][j] ^ key[i][j])
    tmp=[tmp[i:i+4] for i in range(0, 16, 4)]
    return tmp

# a=[[76, 97, 32, 112], [111, 115, 115, 105], [98, 105, 108, 105], [116, 195, 169, 32]]
# b=[[83, 101, 80, 70], [121, 112, 109, 70], [105, 80, 120, 66], [78, 111, 89, 98]]
# print(invaddroundkey(a,b))