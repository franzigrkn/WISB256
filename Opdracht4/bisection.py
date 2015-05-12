def findRoot(f,a,b,epsilon):
    if f(a)==0: #if a is root, return a
        return a
    elif f(b)==0: # if b is root, return b
        return b
    #if f(a)*f(b)>0:
    #    return 
    m=(b+a)/2
    if abs(b-a) <= epsilon:
        return m
    elif f(m)==0:
        return m
    elif f(m)*f(b) > 0:
        return findRoot(f,a,m,epsilon)
    elif f(a)*f(m) > 0:
        return findRoot(f,m,b,epsilon)
        
def findAllRoots(f,a,b,epsilon):
    Roots = []
    for i in range(a,b):
        if f(i)*f(i+0.5)<0:
            x=findRoot(f,i, i+0.5, 0.1)
            Roots.append(x)
        elif f(i+0.5)*f(i+1)<0:
            y=findRoot(f,i+0.5,i+1,0.1)
            Roots.append(y)
    return Roots
    
    
    
    
    
    
    


        
    
        