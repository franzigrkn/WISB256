import bisection
import math

def f(x):
    return math.sin(x)
    
    
root = bisection.findAllRoots(f,-3,3,0.0001)
print(root)