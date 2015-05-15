import math

x=int(input())
y=int(input())
z=int(input())

w=(z*y)/(x**2)
#print(w)
answer = math.asin(w)*(0.5)
print(answer)
goed_answer = "{0:.2f}".format(answer)
print(goed_answer)


