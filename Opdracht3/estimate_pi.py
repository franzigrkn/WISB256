import random
import math
import sys

if len(sys.argv)==4:
    seed = int(sys.argv[3])
    random.seed(seed)

def drop_needle(L):
    x_0=random.random() # uniform in [0,1]
    #y_0=random.random()
    a=random.vonmisesvariate(0,0) #uniform in [0,2*pi]
    x_1= x_0 + L*math.cos(a)
    #y_1 = y_0 + L*math.sin(a)
    #print(x_0)
    #print(y_0)
    #print(a)
    #print(x_1)
    #print(y_1)
    if  x_1 >= 1:
        return True
    elif x_1 <= 0:
        return True
    else:
        return False
        




def hits_needle():
    if len(sys.argv) <3:
        print('Use: estimate_pi.py N L')
        return
    
    N=int(sys.argv[1])
    L=float(sys.argv[2])

    
    if L > 1:
        P=2*L/(math.pi)-2/(math.pi)*(math.sqrt(L**2-1) + 1/(math.sin(L)))+1
        hits=int(P*N)
        print(str(hits) + ' hits in ' + str(N) + ' tries')
        return
    
    count=0
    for i in range(1,N+1):
        if drop_needle(L) == True:
            count=count+1
    print(str(count) + ' hits in ' + str(N) + ' tries')
    pi= (2*N*L)/count
    print('Pi = ' + str(pi))
    return
            

hits_needle()
            
    

    

    
    
    
    
    
    
    

