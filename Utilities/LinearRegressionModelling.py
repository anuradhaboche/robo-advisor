import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import math


def train_test_linear_model(train_dev,N, offset):
  linear_model = LinearRegression()
  prediction_list=[]
  for i in range(offset,len(train_dev)):
    X_train = np.array(range(len(train_dev['Adj Close'][i-N:i])))
    y_train = np.array(train_dev['Adj Close'][i-N:i]) 
    X_train = X_train.reshape(-1, 1) 
    y_train = y_train.reshape(-1, 1)
    linear_model.fit(X_train, y_train)
    predictions = linear_model.predict(X_train)
    prediction_list.append(predictions[0][0])
#   prediction_list = np.array(prediction_list)
#   prediction_list[prediction_list < 0] = 0
  return prediction_list

def execute_linear_model(parameters):
  N_opt=3
  testset=parameters['testset']
  prediction_list=train_test_linear_model(parameters['ticker_stock_data'],N_opt, parameters['num_train']+parameters['num_dev'])
  testset.loc[:, 'pred_N3']=prediction_list
  #print('RMSE=%0.3f'%math.sqrt(mean_squared_error(prediction_list, testset['Adj Close'])))
  #print("R2 = %0.3f" % r2_score(testset['Adj Close'], prediction_list))
  return prediction_list


