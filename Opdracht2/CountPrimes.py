import sys
import math


prime_list=sys.argv[1]

lijst=list(open(prime_list))

pi_N=len(lijst)
#print(pi_N)

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
print( 'N/log(N) = ' + str(A))
print( 'ratio = ' +  str(C))

C_2=0.6601618
twin_pairs=[]
for i in range(0,pi_N -1):
    if lijst[i+1]-lijst[i]==2:
        twin_pairs.append(lijst[i])
twin=list(set(twin_pairs))
#print(twin)

pi_2N=len(twin)
#print(pi_2N)

D= 2 * C_2 * N / (math.log(N))**2

E= (pi_2N)/D

print('pi_2(N) = ' + str(pi_2N))
print('2CN/log(N)^2 = ' + str(D))
print( 'ratio = ' +  str(E))
    


