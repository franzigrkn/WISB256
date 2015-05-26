class Vector:
    ''' Klasse voor Vectoren in R^n
    eigenschappen: dimensie, lijst van floats
    methoden : add, scalar_product, inn_product
    
    '''
    
    __slots__=('dimensie', 'elementen')
    
    def __init__(self, n, scalar=0):
        self.vector=[]
        self.dimensie=n
        for i in range(n):
            self.vector.append(scalar)
        self.elementen=self.vector
            
        
            
        
    def __str__(self):
        answer=''
        #print(type(answer))
        #print(self.elementen[0])
        #print(self.dimensie)
        for i in range(int(self.dimensie)):
            answer= answer + str(self.elementen[i]) + '\n'
        return answer
    

        
        
        
        