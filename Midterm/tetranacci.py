getallen=[0,0,0,1]
for i in range(4,1001):
    x=getallen[i-4]+getallen[i-3]+getallen[i-2]+getallen[i-1]
    getallen.append(x)
#print getallen

#print(getallen[4])

number=int(input())
print(getallen[number])

    
    
