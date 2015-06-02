from Vector import Vector
a=Vector(3)
print(a)
u = Vector(3,[1,2,3])
v = Vector(3, 3.5)
w=u.lincomb(v,10,1)
w=w.scalar(2)
print(w)
print(w.norm())
print(w.inner(u))

from Vector import *
v0=Vector(3,[3,1,0])
v1=Vector(3,[2,2,0])
v2=Vector(3,[5,0,1])
W=GrammSchmidt([v0,v1,v2])
e0=W[0]
e1=W[1]
e2=W[2]
print(e0)
print(e1)
print(e2)

print(e0.inner(e1))
print(e2.inner(e1))
print(e2.inner(e0))

print(e0.norm())

#from Vector import projection_operator
#print(projection_operator(Vector(2,[3,1]), Vector(2,[2,2])))

