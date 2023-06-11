import pandas as pd 
import numpy as np
main=pd.read_csv('price.csv')
print(main.head())
print(main.shape)


X=main[['Year','Quarter']]
print(X)
y=main['Price']
# train_test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)


# Random forest regressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
rf_model=RandomForestRegressor(n_estimators=100,random_state=42)
rf_model.fit(X_train,y_train)
y_pred=rf_model.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
print("Mean Squared Error:",mse)




# support vector regression

from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
svr_model=SVR(kernel='linear')
svr_model.fit(X_train,y_train)
y_pred1=svr_model.predict(X_test)

mse1=mean_squared_error(y_test,y_pred1)
print("Mean Squared SVM error:",mse1)



# # Gradient Boosting Regression

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
gb_model=GradientBoostingRegressor(n_estimators=100,random_state=42)
gb_model.fit(X_train,y_train)
y_pred2=gb_model.predict(X_test)

mse2=mean_squared_error(y_test,y_pred2)
print("Mean Squared Gradient Error:",mse2)