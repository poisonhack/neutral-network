import numpy as np


x = np.array(([2,9],[1,5],[3,6]), dtype = float)
y = np.array(([90],[85],[89]),dtype = float)

x = x/np.amax(x,axis=0)
y = y/100

class Neural(object):
    def __init__(self):
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3

        self.W1 = np.random.randn(self.inputSize,self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize,self.outputSize)
        
    def forward(self,x):
        self.z = np.dot(x,self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2,self.W2)
        o = self.sigmoid(self.z3)
        return o
    def sigmoid(self,s):
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self,s):
        return s * (1-s)
    
    def backward(self, x, y, o):
    
        self.o_error = y - o 
        self.o_delta = self.o_error*self.sigmoidPrime(o) 

        self.z2_error = self.o_delta.dot(self.W2.T) 
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) 

        self.W1 += x.T.dot(self.z2_delta) 
        self.W2 += self.z2.T.dot(self.o_delta)

        
    def train (self, x, y):
        o = self.forward(x)
        self.backward(x, y, o)

NN = Neural()
for i in range(100): 
  print ("Input: \n" + str(x)) 
  print ("Actual Output: \n" + str(y) )
  print ("Predicted Output: \n" + str(NN.forward(x)) )
  print ("Loss: \n" + str(np.mean(np.square(y - NN.forward(x))))) 
  print ("\n")
  NN.train(x, y)
    


