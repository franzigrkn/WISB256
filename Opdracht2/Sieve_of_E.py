import time
T1=time.perf_counter()

def prime(n):
    getallen = list(range(2,n+1, 1))
    for deler in getallen:
        for x in getallen:
            if x%deler==0 and x!=deler:
                getallen.remove(x)
    print(getallen)
    

prime(21)

T2=time.perf_counter()

print('Found x Prime numbers smaller than n in', T2-T1, 'sec.')


document = open('prime.dat')
print(document)
line1='hallo'
document.write(line1)
document.close()




    
    






        
            
            



