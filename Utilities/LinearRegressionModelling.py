import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# def model_linearRegression(parameters):
   
#     trainset= parameters['trainset']
#     testset= parameters['testset']
#     X_train= trainset[['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
#        'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start',
#        'Is_year_end', 'Is_year_start']]
#     y_train= trainset[['Adj Close']]
#     X_test= testset[['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
#        'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start',
#        'Is_year_end', 'Is_year_start']]
#     y_test= testset[['Adj Close']]
#     linear_model= LinearRegression()
#     linear_model.fit(X_train, y_train)

#     linear_predictions=linear_model.predict(X_test)
#     linear_rms= np.sqrt(np.mean(np.power((np.array(y_test)- np.array(linear_predictions)),2)))
#     print('\nRMS with Linear',linear_rms)
#     return 
def model_linearRegression(parameters):
  trainset= parameters['trainset'] 
  testset= parameters['testset']
  X_train= trainset[['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
       'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start',
       'Is_year_end', 'Is_year_start','Volume']]
  y_train= trainset[['Adj Close']]
  linear_model= LinearRegression()
  linear_model.fit(X_train, y_train)
  X_test= testset[['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
       'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start',
       'Is_year_end', 'Is_year_start','Volume']]
  y_test= testset[['Adj Close']]
  linear_predictions=linear_model.predict(X_test)
  linear_rms= np.sqrt(mean_squared_error(y_test, linear_predictions))
  testset.loc[:,'Predictions']=linear_predictions
  ticker_name= parameters['ticker_name']
  parameters= {'testset':testset,'trainset':trainset, 'linear_rms':linear_rms,'ticker_name':ticker_name }
  print(linear_rms)
  return parameters

