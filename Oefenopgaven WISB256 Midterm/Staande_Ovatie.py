maximum=input()
schema=str(input())
list=[]

#print(schema[0])
#print(type(maximum))

for i in range(0, int(maximum)+1):
    list.append(int(schema[i]))
#print(list)


vrienden=[]
for i in range(1, int(maximum)+1):
    if sum(list[:i]) + sum(vrienden) >= i:
        vrienden.append(0)
    elif sum(list[:i]) + sum(vrienden) < i and list[i]==0:
        vrienden.append(0)
    elif sum(list[:i])+sum(vrienden) < i and list[i] > 0:
        x= i-sum(list[:i])-sum(vrienden)
        vrienden.append(x)
    #print(vrienden)

answer=sum(vrienden)
print(answer)
