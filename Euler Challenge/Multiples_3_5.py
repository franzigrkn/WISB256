
multiples=[]
number=int(input())
getallen=list(range(0, number+1))
print(getallen)
for i in range(3,number, 3):
    multiples.append(getallen[i])
for i in range(5, number, 5):
    if getallen[i] not in multiples:
        multiples.append(getallen[i])
    
print(multiples)

answer=sum(multiples)
print(answer)
