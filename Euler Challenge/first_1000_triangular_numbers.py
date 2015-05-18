def prime(n):
    getallen = list(range(0,n))
    getallen[1]=0

    for i in range(1,n):
        if getallen[i]!=0:
            for j in range(2*i,n,i):
                getallen[j]=0
   
    lijst=[1]
    for x in getallen:
        if x!=0:
            lijst.append(x)
    
    return(lijst)

def triangular(i,n,k):
    x=1
    triangular_numbers=[1]
    while i>n:
        for j in range(2,i+1):
            x=x+j
            triangular_numbers.append(x)
        lengte=len(triangular_numbers)
        if lengte > k:
            #print(lengte)
            #print('Done!')
            break
    return triangular_numbers

#print(triangular(101,100, 1000))
        
priemgetallen=prime(100000)
triangle=triangular(101,100, 10)
print(triangle)

def divisor(t,p):
    for x in t:
        divided=[]
        for y in p:
            if x%y==0:
                divided.append(y)
        lengte=len(divided)
        #print(divided)
        if lengte >= 5:
            print(x)
            quit()
            
            
print(divisor(triangle, priemgetallen))


    

