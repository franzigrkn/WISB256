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

from Vector import GrammSchmidt
v0=Vector(2,[3,1])
v1=Vector(2,[2,2])
W=GrammSchmidt([v0,v1])
e0=W[0]
e1=W[1]
print(e0)
print(e1)

print(W[0].inner(W[1]))

print(e0.norm())

