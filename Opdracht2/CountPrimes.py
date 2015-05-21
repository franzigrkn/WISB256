import sys
import math


prime_list=sys.argv[1]

lijst=list(open(prime_list))

pi_N=len(lijst)
print(pi_N)

for i in range(0,pi_N):
    lijst[i]=int(lijst[i])

#print(lijst)



N=(lijst[-1])
#print(N)

A= N/math.log(N)
#print(A)

B=math.log(N)/ N
#print(B)

C= pi_N/A
#print(C)

print('Largest Prime = ' + str(N))
print('pi(N)= ' + str(pi_N))
print( 'N/log(N)) = ' + str(A))
print( 'ratio = ' +  str(C))
    


