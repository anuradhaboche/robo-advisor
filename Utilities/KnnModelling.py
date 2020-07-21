import numpy as np
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler


def model_knn(parameters):
    
  trainset= parameters['trainset']
  testset= parameters['testset']
  X_train= trainset[['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
       'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start',
       'Is_year_end', 'Is_year_start','Volume']]
  y_train= trainset[['Adj Close']]
  X_test= testset[['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
        'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start',
        'Is_year_end', 'Is_year_start','Volume']]
  y_test= testset[['Adj Close']]
  
  scaler= MinMaxScaler(feature_range=(0,1))
  x_train= scaler.fit_transform(X_train)
  x_test= scaler.fit_transform(X_test)
  knn_model=KNeighborsRegressor()
  knn_model.fit(x_train, y_train)
  knn_predictions= knn_model.predict(x_test)
  knn_rms= np.sqrt(mean_squared_error(y_test, knn_predictions))
  print(knn_rms)
  ticker_name= parameters['ticker_name']
  testset.loc[:,'Predictions']=knn_predictions
  parameters= {'testset':testset,'trainset':trainset, 'knn_rms':knn_rms,'ticker_name':ticker_name }
  return parameters