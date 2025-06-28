#gfp2 c est juste les multiple de 2 😂
#x * 3 = x * (2 ⊕ 1) = (x * 2) ⊕ x
#x* 9 = (((x * 2) * 2) * 2) ^ x
#x * 11 = (((x * 2) * 2) ^ x) * 2 ^ x
#x * 13 = (((x * 2) ^ x) * 2) * 2 ^ x
#x * 14 = (((x * 2) ^ x) * 2) ^ x
#MixColumns	2, 3, 1
#InvMixColumns	14, 11, 13, 9
#gfp2,3,9,11,13,14 sont dans le fichier base

# a revoir plus tard

from module.base import gfp2, gfp3, gfp9, gfp11, gfp13, gfp14

import copy

def mixcolumn(state):
	
    n=copy.deepcopy(state)
	
    for i in range(4):
		
        n[i][0]=  (gfp2[state[i][0]] ^ gfp3[state[i][1]] ^ state[i][2] ^ state[i][3]) 
		
        n[i][1] = (state[i][0] ^ gfp2[state[i][1]] ^ gfp3[state[i][2]] ^ state[i][3])
		
        n[i][2] = (state[i][0] ^ state[i][1] ^ gfp2[state[i][2]] ^ gfp3[state[i][3]])
		
        n[i][3] = (gfp3[state[i][0]] ^ state[i][1] ^ state[i][2] ^ gfp2[state[i][3]])
        
    return n 


def invMixColumns(state):

	n = copy.deepcopy(state)
	for i in range(4):
		n[i][0] = (gfp14[state[i][0]] ^ gfp11[state[i][1]] ^ gfp13[state[i][2]] ^ gfp9[state[i][3]])
            
		n[i][1] = (gfp9[state[i][0]] ^ gfp14[state[i][1]] ^ gfp11[state[i][2]] ^ gfp13[state[i][3]])
            
		n[i][2] = (gfp13[state[i][0]] ^ gfp9[state[i][1]] ^ gfp14[state[i][2]] ^ gfp11[state[i][3]])
            
		n[i][3] = (gfp11[state[i][0]] ^ gfp13[state[i][1]] ^ gfp9[state[i][2]] ^ gfp14[state[i][3]])

	return n
