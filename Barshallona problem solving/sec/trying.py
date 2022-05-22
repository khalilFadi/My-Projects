import numpy as np
import matplotlib.pyplot as plt
import random as ran

#the function it self drawing the needed graph 
xs = np.linspace(-10,10,100)
ys = xs ** 2

#this will create a line out of the function 
def grad_square(x):
    return 2 * x
grads = grad_square(xs)


#no idea 
iterantions = 100
x = ran.uniform(-10,10)
step_size = 0.5
print("start as this" ,x)
points  = []
for iteration in range(iterantions):
    #gradient desecent step 
    grad = grad_square(x)
    # direction = -1 if grad < 0 else 1
    x -= grad * step_size
    points.append([x, x ** 2])
print("end as this ", x)
plt.plot(xs,ys)
plt.scatter(*zip(*points), c = "red")
print(x)

plt.show()