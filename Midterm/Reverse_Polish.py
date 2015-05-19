import operator

uitspraak = input()
#print(RPN)

list=[]
def spaties(line):
    lengte=len(line)
    #print(lengte)
    
    index_i=int(uitspraak.find(' '))
    #print(index_i)
    list.append(index_i)
    new_line=line[(index_i)+1:]
    #print(new_line)
    #print(list)
    if len(new_line)<=1:
        krah=0
    else:
        return(spaties(new_line))
    
    #print(list)
    
    lengte_list=len(list)
    #print(lengte_list)
    answer_list=[list[0]]
    
    for i in range(1, lengte_list):
        answer=list[i]+ answer_list[i-1] +1
        answer_list.append(answer)
    
    #print(answer_list)
    return(answer_list)
        
    
print(spaties(uitspraak))
answers=spaties(uitspraak)
print(answers[0])
count=0
for i in answers:
    count=count+1
count=count/2
print(count)

for i in range(0, count):
    result_string = uitspraak[] 
        
        