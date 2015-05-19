
list=[]
def woord(x,y):
    lengte = len(y)
    lengte_x=len(x)
    #print(lengte)
    #print(type(lengte))
    if len(x)==0:
        krah=0
    elif x[0] in y:
        index=int(y.find(x[0]))
        z= y[index+1:]
        #print(z)
        list.append(x[0])
        #print(list)
        new_woord=x[1:]
        if len(new_woord)>0 and new_woord[0]==x[0]:
            new_woord=new_woord[2:]
        return woord(new_woord,z)
    else:
        return False
        
    #print(list)
    #print(len(list))
    answer=''
    for i in list:
        answer=answer+i
    return answer 

    


woordenboek=int(input())
list_woordenboek=[]
for i in range(0,woordenboek):
    woord_i=input()
    list_woordenboek.append(woord_i)
print(list_woordenboek)

swipe=int(input())
list_swipe=[]
for i in range(0,swipe):
    swipe_i=input()
    list_swipe.append(swipe_i)
print(list_swipe)

for x in list_swipe:
    l=len(x)
    for y in list_woordenboek:
        m=len(y)
        if x[0]==y[0] and x[l-1]==y[m-1]:
            if woord(y,x)== y:
                print(y)
        
          
        
            
            

                
            
        
            
        
                
                