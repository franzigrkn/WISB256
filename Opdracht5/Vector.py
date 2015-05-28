import math

class Vector():
    
    def __init__(self, n, constante=0):
        self.vector=[]
        self.dimensie=n
        if type(constante)!=list:
            for i in range(n):
                self.vector.append(constante)
            self.elementen=self.vector
        if type(constante)==list:
            for i in range(n):
                self.vector.append(constante[i])
            self.elementen=self.vector
            
    def __str__(self):
        answer=''
        #print(type(answer))
        #print(self.elementen[0])
        #print(self.dimensie)
        for i in range(int(self.dimensie)):
            answer= answer + str("{0:.6f}".format(self.elementen[i])) + '\n'
        return answer
        
    def lincomb(self, other, alpha,beta):
        lijst=[]
        for i in range(self.dimensie):
            lijst.append(alpha*self.elementen[i]+beta*other.elementen[i])
        return Vector(self.dimensie, lijst)
        
    def scalar(self, alpha):
        lijst=[]
        for i in range(self.dimensie):
            lijst.append(alpha*self.elementen[i])
        return Vector(self.dimensie, lijst)
        
    def inner(self, other):
        answer=0
        for i in range(self.dimensie):
            answer=answer + (self.elementen[i]*other.elementen[i])
            #print(answer)
        return(answer)
        
    def norm(self):
        answer=0
        for i in range(self.dimensie):
            answer= answer + (self.elementen[i]*self.elementen[i])
        answer=math.sqrt(answer)
        return answer
        
        
def projection_operator(u,v):
    constant=v.inner(u)/(u.norm()**2)
    return u.scalar(constant)
    
def orthonormal(u):
    x=u.norm()
    y=1/x
    return u.scalar(y)

def GrammSchmidt(lijst):
    aantal=len(lijst)
    orthogonaal=[lijst[0]]
    for i in range(1,aantal):
        v_i=lijst[i]
        u_i=Vector(len(v_i.elementen),v_i.elementen)
        for j in range(0,i):
            #print('i is' + str(i)+' j is'+ str(j)+ ' u_'+str(i) +'=' +str(u_i))
            u_i = u_i.lincomb(projection_operator(orthogonaal[j],v_i), 1, -1)
            #print('projection =' + str(projection_operator(orthogonaal[j], v_i)))
        orthogonaal.append(u_i)
    for i in range(aantal):
        x=orthonormal(orthogonaal[i])
        orthogonaal[i]=x
        
    return(orthogonaal)
        

        
        
            
        
            
        
    
        
        
        
        
    

        
        
        
        