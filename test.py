
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
        return woord(new_woord,z)
    else:
        return False
        
    #print(list)
    #print(len(list))
    answer=''
    for i in list:
        answer=answer+i
    return answer 
    
        
    
  
    
    
    
#poiuytghjiokn
#poijhgffdsasdfrfd

        
        
            
print(woord('python', 'poiuytghjiokn'))




