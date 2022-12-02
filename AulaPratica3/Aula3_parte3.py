import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import statsmodels.api as sm

#%%
#missing values
df = pd.read_csv("../datasets/kc_house_data.csv")
# Total missing values for each feature
print(df.isnull().sum())

#%%
x_area = df['sqft_living15']
x_area = np. expand_dims(x_area, 1)
y_area = df['price']

lr = lm.LinearRegression()
lr.fit(x_area, y_area)
print('intercept : ', lr.intercept_)
print('coefficient : ', lr.coef_)

#%%
#Analyse Data
independent_variables = ['id','date',
                         'bedrooms', 'bathrooms',
                         'sqft_living','sqft_lot','floors',
                         'waterfront', 'view','condition',
                         'sqft_above','sqft_basement',
                         'yr_built','yr_renovated',
                         'zipcode','lat','long',
                         'sqft_living15','sqft_lot15']
dependent_variables = ['price']

#Atualization of grade values
df.loc[df.grade<=3,'grade'] = 1
df.loc[(df['grade'] > 3) & (df['grade'] < 7),'grade']=2
df.loc[(df['grade'] >= 7) & (df['grade'] <11),'grade']=3
df.loc[df.grade>=11,'grade'] = 4


le = preprocessing.LabelEncoder()
df['date'] = le.fit_transform(df['date'])
print(df['date'])
#%%
#Zipcode
df.zipcode = df.zipcode - 98000
print(df['zipcode'])

#%%
#Bedrooms
print(df['bedrooms'].describe())
boxplot = df.boxplot(column=['bedrooms'])
#%%
#Bathrooms
print(df['bathrooms'].describe())
boxplot = df.boxplot(column=['bathrooms'])
#%%
#Sqft_living
print(df['sqft_living'].describe())
boxplot = df.boxplot(column=['sqft_living'])
#%%
#Sqft_lot
print(df['sqft_lot'].describe())
boxplot = df.boxplot(column=['sqft_lot'])
#%%
#Floors
print(df['floors'].describe())
boxplot = df.boxplot(column=['floors'])
#%%
#sqft_basement
print(df['sqft_basement'].describe())
boxplot = df.boxplot(column=['sqft_basement'])
#%%
#sqft_above
print(df['sqft_above'].describe())
boxplot = df.boxplot(column=['sqft_above'])
#%%
#yr_built
print(df['yr_built'].describe())
boxplot = df.boxplot(column=['yr_built'])
#%%
#Yr_renovated
print(df['yr_renovated'].describe())
boxplot = df.boxplot(column=['yr_renovated'])
#%%
#Sqft_living15
print(df['sqft_living15'].describe())
boxplot = df.boxplot(column=['sqft_living15'])

#%%
#Sqft_lot15
print(df['sqft_lot15'].describe())
boxplot = df.boxplot(column=['sqft_lot15'])

#%%
#Faz sentido termos meio andar?
print(df.floors.unique())
#Faz sentido termos 1.75 de casas de banho?
print(df.bathrooms.unique())
#33 quartos? Remove?
print(df.bedrooms.unique())

#devo normalizar?
print(df['yr_renovated'].unique())

#%%

#%%

#%%
