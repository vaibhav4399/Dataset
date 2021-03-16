from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

data = pd.read_csv("mydata2.csv")



train, test = train_test_split(data,test_size=0.1,random_state=0)

x_train = train.drop(['Yield'], axis='columns')
y_train = train['Yield']
x_test = test.drop(['Yield'], axis='columns')
y_test = test['Yield']


best_features = SelectKBest(score_func=f_regression, k="all")
top_features = best_features.fit(x_train,y_train)
scores = pd.DataFrame(top_features.scores_)
columns = pd.DataFrame(x_train.columns)
featureScores = pd.concat([columns, scores], axis=1)
featureScores.columns = ['Features','Scores']
print(featureScores.nlargest(5,'Scores'))

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import xgboost as xgb
from sklearn.model_selection import cross_val_score
rr = RandomForestRegressor(n_estimators=1000,n_jobs=-1,random_state=0)
gbr = GradientBoostingRegressor(random_state=0)
xgb = xgb.XGBRegressor()


def display_scores(scores):
    print("Scores: ", scores)
    print("Mean: ", scores.mean())
    print("Standard Deviation: ", scores.std())

print("Random Forest Regressor Scores")
scores = cross_val_score(rr, x_train, y_train, scoring='neg_mean_squared_error')
random_forest_scores = np.sqrt(-scores)
display_scores(random_forest_scores)
print("\n")

print('Gradient Boosting Regressor Scores')
scores = cross_val_score(gbr, x_train, y_train, scoring='neg_mean_squared_error', cv=5)
gradient_boosting_regressor = np.sqrt(-scores)
display_scores(gradient_boosting_regressor)
print("\n")

print("xGB Scores")
scores = cross_val_score(xgb, x_train, y_train, scoring='neg_mean_squared_error', cv=5)
xgb_regressor = np.sqrt(-scores)
display_scores(xgb_regressor)
print("\n")

print(x_test)
rr.fit(x_train, y_train)
pred = rr.predict(x_test)


errors = abs(pred - y_test)
print('Average absolute error:', round(np.mean(errors), 2), 'degrees.')
mape = 100*(errors / y_test)
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')


compare = pd.DataFrame()
compare['y_true'] = y_test
compare['y_predict'] = pred
