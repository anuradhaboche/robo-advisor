from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
import pandas as pd
from math import sqrt

def model_autoArima(parameters):
    trainset= parameters['trainset']
    testset= parameters['testset']
    training=trainset['Adj Close']
    testing= testset['Adj Close']
    model_arima = auto_arima(training, trace=True, error_action='ignore', suppress_warnings=True)
    model_arima.fit(training)
    forecast = model_arima.predict(n_periods=len(testing))
    arima_predictions = pd.DataFrame(forecast,index = testing.index,columns=['Prediction'])
    arima_rms = sqrt(mean_squared_error(testing,forecast))
    print('RMS for Auto Arima', arima_rms)
    ticker_name= parameters['ticker_name']
    testset.loc[:,'Predictions']=forecast
    print(testset.head())
    parameters= {'testset':testset,'trainset':trainset, 'arima_rms':arima_rms,'ticker_name':ticker_name }
    return parameters