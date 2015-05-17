import math
def prime(n):
    getallen = list(range(0,n))
    getallen[1]=0

    for i in range(1,n):
        if getallen[i]!=0:
            for j in range(2*i,n,i):
                getallen[j]=0
    #print(getallen)
    primes=[]    
    for i in range(0,n):
        if getallen[i]!=0:
            primes.append(getallen[i])
            #print(primes)
        
    return primes
            

def divisors(lijst):
    prime_divisors=[]
    n=len(lijst)
    for i in range(0,(n/2)+1):
        if number % lijst[i]==0:
            prime_divisors.append(lijst[i])
    
    return(prime_divisors)
            
    
number=input()
prime_lijst=prime(number)


answer_list=divisors(prime_lijst)
print(answer_list)


