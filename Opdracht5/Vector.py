import math

class Vector():
    ''' Klasse voor Vectoren in R^n
    eigenschappen: dimensie, lijst van floats
    methoden : add, scalar_product, inn_product
    
    '''
    
    #__slots__=('dimensie', 'elementen', 'vector')
    
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
            lijst.append (alpha*self.elementen[i]+beta*other.elementen[i])
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
    constant=u.inner(v)/u.norm()
    return u.scalar(constant)
    
def orthonormal(u):
    x=u.norm()
    y=1/x
    return u.scalar(y)

def GrammSchmidt(lijst):
    aantal=len(lijst)
    u_1=orthonormal(lijst[0])
    orthogonaal=[u_1]
    for i in range(2,aantal+1):
        u_i=lijst[i-1]
        for j in range(1,i):
            u_i = u_i.lincomb(projection_operator(orthogonaal[j-1],lijst[i-1]), 1, -1)
            u_i=orthonormal(u_i)
    orthogonaal.append(u_i)
    #print(orthogonaal)
    return(orthogonaal)
        

        
        
            
        
            
        
    
        
        
        
        
    

        
        
        
        