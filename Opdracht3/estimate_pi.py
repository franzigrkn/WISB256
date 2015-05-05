import random
import math

x = random.random() # uniform in [0,1]
y = random.random()
z = random.vonmisesvariate(0,0) #uniform in [0,2*pi]

def drop_needle(L):
    x_0=x
    y_0=y
    a=z
    x_1= x_0 + L*math.cos(a)
    y_1 = y_0 + L*math.sin(a)
    print(x_0)
    print(y_0)
    print(a)
    print(x_1)
    print(y_1)
    if  x_1 >= 1:
        return True
    elif x_1 <= 0:
        return True
    else:
        return False
        

print(drop_needle(0.7))