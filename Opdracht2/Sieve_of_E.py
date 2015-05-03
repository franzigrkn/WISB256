import sys
import time
T1=time.perf_counter()

def prime(n):
    getallen = list(range(0,n))
    getallen[1]=0

    for i in range(1,n):
        if getallen[i]!=0:
            for j in range(2*i,n,i):
                getallen[j]=0
    
    return getallen
    
T2=time.perf_counter()

n=int(sys.argv[1])
bestandsnaam = sys.argv[2]

document = open(bestandsnaam ,  'w')
for x in prime(n):
    if x!=0:
        document.write(str(x) + '\n')
document.close()
    

    
num_line=sum(1 for line in open('prime.dat'))




print('Found ' + str(num_line) + ' Prime numbers smaller than ' + str(n) + ' in ' + str(T2-T1) + ' sec.')







            
            


    
    
            
    
    





                
        

    
