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


    

answer_lijst = prime(2000000)
lengte = len(answer_lijst)
answer= sum(answer_lijst)
print(answer)
