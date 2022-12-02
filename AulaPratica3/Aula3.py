import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import statsmodels.api as sm


#%%
df = pd.read_csv("RegressãoMultivariada.csv")

independent_variables = ['Size', 'Rooms']
dependent_variables = ['Price']

X = df[independent_variables]
y = df[dependent_variables]

lr = lm.LinearRegression()

lr2 = sm.OLS(y, X).fit()

X_train, X_test, y_train, y_test = \
    train_test_split(X,
                     y,
                     train_size =.8,
                     random_state =1)

lr.fit(X_train,y_train)
print(lr.coef_)
#%%
y_train_pred = lr.predict(X_train)
y_test_pred = lr.predict(X_test)
y_pred = lr.predict(X)# full data


print('Train MAE :',
      metrics.mean_absolute_error(y_train,y_train_pred))
print('Train RMSE',
      np.sqrt(metrics.mean_squared_error(y_train,y_train_pred)))

#%%
predictedCO2 = lr.predict([[1800, 3]])
print(predictedCO2)
