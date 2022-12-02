import numpy as np
import pandas as pd
#%%
dataset = pd.read_csv("RegressaoUnivariada.csv");


x1 = dataset['Population'].to_numpy()
x0 = np.ones(len(x1))
x = np.array([[x0],[x1]])

y = dataset['Profit'].to_numpy()
theta = np.zeros(2)
print(theta)
theta = np.zeros((x.shape[1],1))
print(theta)
#x = np.stack()





#%%
def computaCusto(x,y,theta):
    m = np.shape(y)[0]
    x0theta0 = x[0] * theta[0]
    x1theta1 = x[1] * theta[1]
    htheta = np.array([[x0theta0],[x1theta1]])
    htheta = np.sum(htheta, axis = 1)
    dif = htheta-y
    dif = dif * x
    dif = np.power(dif,2)
    sumDif = np.sum(dif)
    j = 1/(2*m)*sumDif
    return j
print(computaCusto(x,y,theta))

#%%
