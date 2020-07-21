import pandas as pd 
import numpy as np
import time
from PreprocessStocksData import *
from LinearRegressionModelling import * 
from KnnModelling import *
from AutoArimaModelling import *
from LSTMModelling import *
from PlottingModels import *
import json

pd.options.mode.chained_assignment = None
ticker_stock_data= pd.DataFrame()
parameters={}
start= time.time()
ticker_stock_data=fetch_data_from_db('GOOG')
ticker_stock_data=preprocess_ticker_data(ticker_stock_data)
parameters=split_data(ticker_stock_data)
parameters=model_linearRegression(parameters)
# parameters=model_knn(parameters)
# parameters=model_autoArima(parameters)
# parameters=model_LSTM(parameters)
# current_price(parameters)
# forecast_price(parameters)
convert_to_json(parameters)

print("\nTime to load data: {} seconds".format(time.time() - start))