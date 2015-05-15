maximum=input()
schema=str(input())
list=[]

#print(schema[0])
#print(type(maximum))

for i in range(0, int(maximum)+1):
    list.append(int(schema[i]))
#print(list)
#print(sum(list[0:2]))
vrienden=[]
for i in range(1, int(maximum)+1):
    if sum(list[:i]) >= i:
        vrienden.append(0)
    elif sum(list[:i]) < i and list[i]==0:
        vrienden.append(0)
    elif sum(list[:i])+sum(vrienden) < i and list[i] > 0:
        x= i-sum(list[:i])
        vrienden.append(x)
#print(vrienden)

answer=sum(vrienden)
print(answer)
