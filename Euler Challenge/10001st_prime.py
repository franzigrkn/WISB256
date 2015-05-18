def prime(n):
    getallen = list(range(0,n))
    getallen[1]=0

    for i in range(1,n):
        if getallen[i]!=0:
            for j in range(2*i,n,i):
                getallen[j]=0
   
    lijst=[]
    for x in getallen:
        if x!=0:
            lijst.append(x)
    
    return(lijst)


    

antwoord = prime(1000000)
aantal=len(antwoord)
print(aantal)
if aantal>= 10001:
    print('yes')
    print(antwoord[10000])






        