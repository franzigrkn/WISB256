def findRoot(f,a,b,epsilon):
    if f(a)==0: #if a is root, return a
        return a
    elif f(b)==0: # if b is root, return b
        return b
    
    m=(b-a)/2
    print(m)
    if abs(b-a) < epsilon:
        return m
    elif f(m)==0:
        return m
    elif f(m)*f(b) > 0:
        return findRoot(f,a,m,epsilon)
    elif f(a)*f(m) > 0:
        return findRoot(f,m,b,epsilon)
    

    
        

def f(x):
    x-1
    return x-1


print(findRoot(f,0,2,0.1))

        
    
        