import time
T1=time.perf_counter()

def prime(n):
    getallen = list(range(2,n+1, 1))
    for deler in getallen:
        for x in getallen:
            if x%deler==0 and x!=deler:
                getallen.remove(x)
    print(getallen)
   

prime(10000)


T2=time.perf_counter()
print('Time required', T2-T1, 'sec.')
print('Found x Prime numbers smaller than n in', T2-T1 , 'sec.')


fin = open( 'prime.dat', 'w')
print(fin)
line1 = 'hallo'
fin.write(line1)
line2 = 'hallo'
fin.write(line2)
fin.close()


    
    






        
            
            



