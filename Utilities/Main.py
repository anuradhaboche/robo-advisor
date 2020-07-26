import pandas as pd 
import numpy as np
import time
from PreprocessStocksData import *
from LinearRegressionModelling import * 
# from KnnModelling import *
# from AutoArimaModelling import *
# from LSTMModelling import *
from PlottingModels import *
# from MovingAverageModelling import *
import json
import warnings
warnings.filterwarnings('ignore')

def prediction(ticker):
    pd.options.mode.chained_assignment = None
    ticker_stock_data= pd.DataFrame()
    parameters={}
    start= time.time()
    ticker_stock_data=fetch_data_from_db(ticker)
    ticker_stock_data=preprocess_ticker_data(ticker_stock_data)
    display_parameters= display_columns(ticker_stock_data)
    parameters=split_data(ticker_stock_data)
    prediction_list=execute_linear_model(parameters)
    current_price(display_parameters)
    display_parameters=forecast_price(display_parameters,prediction_list)


    # prediction_list=execute_linear_model(parameters)
    # prediction_list=execute_lstm_model(parameters)
    # prediction_list=execute_moving_average(parameters)
    # prediction_list=execute_arima_model(parameters)

    json = convert_to_json(display_parameters)
    print("\nTime to load data: {} minutes".format((time.time() - start)/60.0))
    return json

# prediction('WFC')