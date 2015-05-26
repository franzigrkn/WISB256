import math

class Vector:
    ''' Klasse voor Vectoren in R^n
    eigenschappen: dimensie, lijst van floats
    methoden : add, scalar_product, inn_product
    
    '''
    
    __slots__=('dimensie', 'elementen')
    
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
            answer= answer + str(self.elementen[i]) + '\n'
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
        
        
        
        
    

        
        
        
        