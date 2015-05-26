import bisection
import math

def f(x):
    return math.cos(x)

    
root = bisection.findRoot(f,0,2,0.1)
print(root)