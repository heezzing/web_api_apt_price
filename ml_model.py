import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/Users/hk/coding/project3/apt_data.csv', encoding='cp949')
df1 = df

model = LinearRegression()

target = ['거래금액(만원)']
features = ['건축년도']

train, test = train_test_split(df1, test_size=0.2, random_state=2)

X_train_gov=train[features]
y_train_gov=train[target]
X_test_gov=test[features]
y_test_gov=test[target]

model.fit(X_train_gov,y_train_gov)
y_pred_gov = model.predict(X_train_gov)

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_squared_log_error
MAE=mean_absolute_error(y_train_gov, y_pred_gov)
MSE=mean_squared_error(y_train_gov,y_pred_gov)
RMSE=np.sqrt(MSE)
R2= r2_score(y_train_gov, y_pred_gov)

print("MAE :",MAE)
print("MSE :",MSE)
print("RMSE :",RMSE)
print("R2 :",R2)
