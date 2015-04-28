
def prime(n):
    getallen = list(range(2,n+1, 1))
    for deler in getallen:
        for x in getallen:
            if x%deler==0 and x!=deler:
                getallen.remove(x)
                print(getallen)
            
       
prime(21)
        
            
            



