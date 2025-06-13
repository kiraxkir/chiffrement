

def shiftrows(message):
    permut= [0, 1, 2, 3]
    for i in range(4):
        message[i]=decalage(message[i],permut[i])
    return message

def decalage(message,permut):
    temp=[c for c in message]
    temp2=[0,0,0,0]
    for i in range(permut):
        for j in range(4):
            temp2[(3+j)%4] = temp[j]
        temp=[c for c in temp2]
    return temp   
 


m=[[32, 105, 110, 102], [111, 114, 109, 97], [116, 105, 99, 105], [100,200,300,400]]



def invshiftrows(message):
    permut= [0, 1, 2, 3]
    for i in range(4):
        message[i]=decalageInv(message[i],permut[i])
    return message
            
def decalageInv(message, permut):
    tmp = [c for c in message]
    tmp2 = [0, 0, 0, 0]
    for i in range(permut):
        for j in range(4):
            tmp2[j] = tmp[(3+j)%4]
        tmp = [x for x in tmp2]
    
    return tmp
