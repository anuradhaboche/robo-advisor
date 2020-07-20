import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
def prepData(parameters):
  ticker_stock_data= parameters['ticker_stock_data']
  trainset= parameters['trainset']
  testset= parameters['testset']
  dataset= ticker_stock_data[['Adj Close']].values
  train = trainset[['Adj Close']].values
  test = testset[['Adj Close']].values
  scaler = MinMaxScaler(feature_range=(0, 1))
  scaled_data = scaler.fit_transform(dataset)
  x_train, y_train = [], []
  for i in range(100,len(train)):
      x_train.append(scaled_data[i-100:i,0])
      y_train.append(scaled_data[i,0])
  x_train, y_train = np.array(x_train), np.array(y_train)
  x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))

  data= ticker_stock_data[['Adj Close']]
  inputs = data[len(data) - len(test) - 100:].values
  inputs = inputs.reshape(-1,1)
  inputs  = scaler.transform(inputs)
  X_test = []
  for i in range(100,inputs.shape[0]):
      X_test.append(inputs[i-100:i,0])
  X_test = np.array(X_test)
  X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))

  splitData= {'x_train':x_train, 'y_train':y_train,'X_test':X_test , 'test':test, 'scaler':scaler}

  return splitData

def model_LSTM(parameters):
  splitData=prepData(parameters)
  x_train= splitData['x_train']
  y_train= splitData['y_train']
  X_test= splitData['X_test']
  scaler= splitData['scaler']
  test= splitData['test']
  model = Sequential()
  model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
  model.add(LSTM(units=50))
  model.add(Dense(1))
  model.compile(loss='mean_squared_error', optimizer='adam')
  model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)
  predictions = model.predict(X_test)
  lstm_predictions = scaler.inverse_transform(predictions)
  lstm_rms=np.sqrt(np.mean(np.power((test-lstm_predictions),2)))
  print('RMS with LTSM',lstm_rms)
  return