
import numpy as np
import pandas as pd
import math
from sklearn.metrics import mean_squared_error

def moving_average_prediction(ticker_stock_data, N, offset):
  pred_list = pd.Series(ticker_stock_data['Adj Close']).rolling(window=N).mean().tolist()
  pred_list = np.concatenate((np.array([np.nan]), np.array(pred_list[:-1])))
  pred_list = np.array(pred_list)
  pred_list[pred_list < 0] = 0
  pred_list= pred_list[offset:]
  return pred_list

def execute_moving_average(parameters):
  RMSE=[]
  N_opt=2
  ticker_stock_data= parameters['ticker_stock_data']
  num_train= parameters['num_train']
  num_train_dev= parameters['num_train_dev']
  testset= parameters['testset']
  prediction_list= moving_average_prediction(ticker_stock_data, N_opt, num_train_dev)
  testset.loc[:,'Pred_N'+ str(N_opt)]= prediction_list
  print("R2 = %0.3f" %math.sqrt(mean_squared_error(prediction_list, testset['Adj Close'])))
  return prediction_list