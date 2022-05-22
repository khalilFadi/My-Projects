import numpy as np
import pandas as pd

#print(pd.read_csv("iris_training.csv"))

#this will take the first 3 lines and saving them in X
#the .T will transpose and change the rows to colums 
x = np.array(pd.read_csv("iris_training.csv").iloc[:, :4]).T

#print(x.shape) to get the size which will be (120, 4) in 
#this situation 

#this will write the same thing but for the last time 
#read_csv will organize each row as a seperate object 
GT = np.array(pd.read_csv("iris_training.csv").iloc[:, -1])

#yay we got to the model finally
def model(y, param):
    #param is the matrix of the shape (4, 3)
    #matmul will usualy maultiply matrises 
        #for example:
            #a = [[1,0],[0,1]] b = [[4,1],[2,2]] 
            #a * b = [4, 1] [2, 2]
    return np.matmul(param, x)
param = np.random.rand(3, 4)
output = model(x, param)
def loss(output, gt):
    return ((gt - output ) ** 2).sum()

def loss_grad(out, gt, X):

    return 2 * np.matmul((out - gt), X.T))

print(loss(output, GT))
print(loss_grad(output, GT, x))
print(GT)