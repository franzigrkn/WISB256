

import numpy as np
import scipy as sp
from scipy.linalg import eigvals
from scipy.integrate import odeint




class Lorenz():
    
    def __init__(self, lijst, sigma=10, rho=28, beta=(8/3)):
        self.x0=lijst[0]
        self.y0=lijst[1]
        self.z0=lijst[2]
        
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
    
    def functies(self, w, t):
        x_dot=self.sigma*(w[1]-w[0])
        y_dot=w[0]*(self.rho-w[2])-w[1]
        z_dot=w[0]*w[1]-(self.beta)*w[2]
        
        result=np.array([x_dot, y_dot, z_dot])
        #print(result)
        return result
        
        
    def solve(self, T, dt):
    
        self.times=np.arange(0,T,dt)
        #print(self.times)
        self.initials=[self.x0, self.y0, self.z0]
        self.oplossing= odeint(self.functies, self.initials, self.times)
        #self.x=self.oplossing[:,0]
        #self.y=self.oplossing[:,1]
        #self.z=self.oplossing[:,2]
        #return np.array([self.x, self.y, self.z])
        return self.oplossing
        
    def df(self, u):
        matrix=np.array([[-self.sigma, self.sigma, 0],
                         [self.rho-u[2], -1, -u[0]],
                         [u[1], u[0], -self.beta]])
        return matrix
    
        
    def isStable(self,u):
        eigenwaarden=eigvals(self.df(u))
        print(eigenwaarden)
        if eigenwaarden[0]<0 and eigenwaarden[1]<0 and eigenwaarden[2]<0:
            return True
        else:
            return False
        
    
     
            
            
            
            
            
            
            
            
            
    