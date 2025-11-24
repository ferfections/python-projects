from dataclasses import dataclass
import numpy as np
import keras as kr

class Neuron:
    
    def __init__(self, i, w, b):
        self.inputs = np.array(i)
        self.weights = np.array(w)
        self.bias = b
        self.output = np.dot(self.weights, self.inputs) + self.bias

    def activation(self):
        return 1/(1+ np.exp(- self.output))
    
    def derivada_sigmo(self):
        a = self.activation()
        return(a * (1 - a))
    
def main():
    a1 = [1.0, 0.5, 1.0]
    w2 = [[1.0, 0.5, 0.2],
          [0.7, 1.0, 0.1],
          [0.0, 0.9, 0.3],
          [0.5, 0.6, 0.8]]
    w3 = [[0.9, 0.6, 0.0, 0.4],
          [0.6, 0.9, 0.8, 0.0]]
    b2 = [0.43, 0.03, 0.56, 0.67]
    b3 = [0.53, 0.34]
    y = [1.0, 0.1]

    neuron1 = Neuron(a1, w2, b2)
    res = neuron1.activation()
    print(res)



    

if __name__ == "__main__":
    main()