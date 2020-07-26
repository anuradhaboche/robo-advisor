from sklearn.metrics import mean_squared_error
import pandas as pd
from math import sqrt
from statsmodels.tsa.arima_model import ARIMA
import math

def train_predict_arima(train, arima_order, devset):
    predictions = list()
    history = [x for x in train]
    for t in range(len(devset)):
        model = ARIMA(history, order=arima_order)
        model_fit = model.fit(disp=0)
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(devset[t])
    return predictions

def execute_arima_model(parameters):
  testset= parameters['testset']
  prediction_list= train_predict_arima(parameters['ticker_stock_data']['Adj Close'], (0,1,0), testset['Adj Close'])
  testset.loc[:, 'Predictions']=prediction_list
  print('RMSE=%0.3f'%math.sqrt(mean_squared_error(prediction_list, testset['Adj Close'])))
  return prediction_list

