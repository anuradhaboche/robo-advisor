import pandas as pd 
import numpy as np
import time
from PreprocessStocksData import *
from LinearRegressionModelling import * 
from KnnModelling import *
from AutoArimaModelling import *
from LSTMModelling import *

ticker_stock_data= pd.DataFrame()
parameters={}
start= time.time()
ticker_stock_data=fetch_data_from_db('GOOG')
ticker_stock_data=preprocess_ticker_data(ticker_stock_data)
parameters=split_data(ticker_stock_data)
model_linearRegression(parameters)
# model_knn(parameters)
# model_autoArima(parameters)
# model_LSTM(parameters)
print("\nTime to load data: {} seconds".format(time.time() - start))