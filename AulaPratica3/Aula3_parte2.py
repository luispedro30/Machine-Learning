#%%
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn import metrics, preprocessing
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import statsmodels.api as sm


#%%
df = pd.read_csv("../datasets/Grade_Set_1.csv")

independent_variables = ['Hours_Studied']
dependent_variables = ['Test_Grade']

X=df[independent_variables]
#X=np.expand_dims(X,1)
y=df[dependent_variables]

lr = lm.LinearRegression()
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)





#%%
df2 = pd.read_csv("../datasets/Grade_Set_2.csv")
print(df2)

independent_variables = ['Hours_Studied']
dependent_variables = ['Test_Grade']

X2=df2.Hours_Studied
y2=df2.Test_Grade

lr = lm.LinearRegression()

for deg in [1, 2, 3, 4, 5, 6]:
    lr.fit(np.vander(X2, deg + 1), y2)
    y_lr = lr.predict(np.vander(X2, deg + 1))
    plt.plot(X2, y_lr, label='degree' + str(deg))
    plt.legend(loc=2)
    print("R- Squared for degree",
           str(deg),
           '=',
           r2_score(y2,y_lr))

#%%
df3 = pd.read_csv("../datasets/Housing_Modified.csv")


independent_variables = ['lotsize','bedrooms', 'bathrms',
'stories','driveway',
'recroom', 'fullbase','gashw','airco',
'garagepl','prefarea']
dependent_variables = ['price']

#Boolean to numeric
lb = preprocessing.LabelBinarizer()
df3['driveway']= lb.fit_transform(df3['driveway'])
df3['recroom'] = lb.fit_transform(df3['recroom'])
df3['fullbase'] = lb.fit_transform(df3['fullbase'])
df3['gashw'] = lb.fit_transform(df3['gashw'])
df3['airco'] = lb.fit_transform(df3['airco'])
df3['prefarea'] = lb.fit_transform(df3['prefarea'])

#Categoric to numeric
le = preprocessing.LabelEncoder()
df3['stories'] = le.fit_transform(df3['stories'])

"""
ohe = OneHotEncoder()
enc_df = pd.DataFrame(ohe.fit_transform(df3[['stories']]).toarray(), columns=ohe.get_feature_names_out())
df3 = df3.join(enc_df)
print(df3.sample(20))
"""


x3 = df3[independent_variables]
y3 = df3[dependent_variables]

#check the types of attibutes
print(x3.dtypes)
#x3['driveway'] = np.array(x3['driveway'], dtype=float)


#%%
from statsmodels.stats.outliers_influence import variance_inflation_factor

thresh = 10
for i in np.arange(0, len(independent_variables)):
    vif = [variance_inflation_factor(x3[independent_variables].values,ix)
        for ix in range(x3[independent_variables].shape[1])]
    maxloc = vif.index(max(vif))
    if max(vif) > thresh:
        print('vif :', vif)
        print('dropping', x3[independent_variables].columns[maxloc],
              'at index', maxloc)
        del independent_variables[maxloc]
    else:
        break

print('Final variables :',independent_variables)
#%%
X_train , X_test , y_train , y_test = train_test_split (x3[independent_variables], y3, train_size =.8,
                                                        random_state =1)

lr = lm.LinearRegression()
lr.fit(X_train,y_train)
print(lr.coef_)
print(lr.intercept_)

#make predictions on the training dataset
y_train_pred = lr.predict(X_train)
print('Train MAE : ',metrics.mean_absolute_error(y_train,y_train_pred))
print('Train RMSE',np.sqrt(metrics.mean_squared_error(y_train,y_train_pred)))

#make predictions on the testing set
y_test_pred = lr.predict(X_test)
print('Train MAE : ',metrics.mean_absolute_error(y_test,y_test_pred))
print('Train RMSE',np.sqrt(metrics.mean_squared_error(y_test,y_test_pred)))
#%%
