import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from PreprocessStocksData import get_x_y
import math
from sklearn.metrics import mean_squared_error

def execute_lstm_model(parameters):

  N_opt=41; lstm_units_opt=50; dropout_prob_opt=1; 
  epoch_opt=1; batch_size_opt=1; optimizer_opt='adam'
  trainset=parameters['trainset']; ticker_stock_data= parameters['ticker_stock_data']; train_dev= parameters['train_dev']
  num_train= parameters['num_train']; num_dev= parameters['num_dev']
  scaler= MinMaxScaler(feature_range=(0,1))

  train_dev_scaled= scaler.fit_transform(np.array(train_dev['Adj Close']).reshape(-1,1))
  x_train_dev, y_train_dev= get_x_y(train_dev_scaled, N_opt, N_opt)

  test_scaled  = scaler.transform(np.array(ticker_stock_data['Adj Close']).reshape(-1,1))
  x_test, y_test = get_x_y(test_scaled, N_opt, num_train+num_dev)
  
  rmse, prediction_list = train_test_lstm_model(x_train_dev, y_train_dev, x_test, y_test, scaler, lstm_units_opt, dropout_prob_opt, optimizer_opt, 
        epoch_opt, batch_size_opt)
  print("RMSE on test set = %0.3f" % rmse)
  return prediction_list

def train_test_lstm_model(x_train_scaled,y_train_scaled,x_dev_scaled,y_dev_scaled,scaler, lstm_units_opt,dropout_prob_opt,optimizer_opt,epoch_opt,batch_size_opt):
  model= Sequential()
  model.add(LSTM(units=lstm_units_opt,return_sequences=True,input_shape=(x_train_scaled.shape[1],1)))
  model.add(Dropout(dropout_prob_opt))
  model.add(LSTM(units=lstm_units_opt))
  model.add(Dropout(dropout_prob_opt))
  model.add(Dense(1))
  model.compile(loss='mean_squared_error', optimizer=optimizer_opt)
  model.fit(x_train_scaled, y_train_scaled, epochs=epoch_opt, batch_size=batch_size_opt, verbose=0)
  forecast=model.predict(x_dev_scaled)
  forecast_inv=scaler.inverse_transform(forecast)
  y_dev = scaler.inverse_transform(y_dev_scaled)
  rmse = math.sqrt(mean_squared_error(y_dev, forecast_inv))

  return rmse, forecast_inv