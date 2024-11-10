import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return(x+3)**2

def derivative(x):
    return 2*(x+3)

def gradient(starting_x,learning_rate,itr):
    x=starting_x
    history=[]

    for i in range(itr):
        grad=derivative(x)
        x=x-learning_rate*grad
        history.append(x)
    
    return x,history

starting_x=2
learning_rate=0.1
itr=50

final_x ,history =gradient (starting_x,learning_rate ,itr)
print(f'local minima found at x={final_x}')

x_val=np.linspace(-10,5,100)
y_val=function(x_val)

plt.plot(x_val ,y_val)
plt.scatter(history ,[function(x) for x in history], color='red', label='grd',zorder=5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show() 