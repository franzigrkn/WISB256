def findRoot(f,a,b,epsilon):
    if f(a)==0: #if a is root, return a
        return a
    elif f(b)==0: # if b is root, return b
        return b
    if f(a)*f(b)>0:
        return
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
    n=100000
    l=(b-a)/n
    for i in range(n):
        if f(a+i*l)*f(a+(i+1)*l)<=0:
            x=findRoot(f,a+i*l, a+(i+1)*l, epsilon)
            Roots.append(x)
    return list(set(Roots))
    
    
    
    
    
    
    


        
    
        