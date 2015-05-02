import sys
import time
T1=time.perf_counter()

def prime(n):
    getallen = list(range(2,int(n**(0.5)), 1))
    for deler in getallen:
        for x in getallen:
            if x%deler==0 and x!=deler:
                getallen.remove(x)
    
    return getallen
n=10000
T2=time.perf_counter()

n=int(sys.argv[1])
bestandsnaam = sys.argv[2]

    
document = open(bestandsnaam ,  'w')
for x in prime(n):
    document.write(str(x) + '\n')
document.close()
    
size=(len(prime(n)))



print('Found ' + str(size) + ' Prime numbers smaller than ' + str(n) + ' in ' + str(T2-T1) + ' sec.')















    
    






        
            
            



