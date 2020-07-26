import pandas as pd 
import numpy as np
import sqlite3
from  fastai.tabular import add_datepart
from sklearn.model_selection import train_test_split
import datetime

def fetch_data_from_db(ticker):
    connection = sqlite3.connect('/Users/anuradha/Desktop/Database/portfolio_db.db')
    cursor=connection.execute('Select * from stocks_data where Ticker=?', (ticker,))
    ticker_stock_data= pd.DataFrame(cursor.fetchall())
    ticker_stock_data.columns=[x[0] for x in cursor.description]
    # print(ticker_stock_data.head())
    # preprocess_ticker_data(ticker_stock_data)
    return ticker_stock_data


def preprocess_ticker_data(ticker_stock_data):
    ticker_stock_data['Date'] = pd.to_datetime(ticker_stock_data.Date,format='%Y-%m-%d')
    ticker_stock_data.sort_values(by='Date', inplace=True)
    ticker_stock_data.index= ticker_stock_data['Date']
    # ticker_stock_data.drop(columns=['Date'], inplace=True, axis=1)
    # add_datepart(ticker_stock_data, 'Date', drop=False)
    # ticker_stock_data.drop(labels='Elapsed', axis=1,inplace=True)
    ticker_stock_data.Close.fillna(method='ffill', inplace=True)
    ticker_stock_data['Adj Close'].fillna(method='ffill', inplace=True)
    return ticker_stock_data

def split_data(ticker_stock_data):
      ticker_stock_data.index= ticker_stock_data['Date']
      trainset=ticker_stock_data.loc['1990-01-01':'2010-12-31'][['Adj Close']]
      devset=ticker_stock_data.loc['2011-01-01':'2015-12-31'][['Adj Close']]
      testset= ticker_stock_data.loc['2016-01-01': '2019-12-31'][['Adj Close']]
      ticker_name= ticker_stock_data['Ticker'][0]
      train_dev= trainset.append(devset)
      num_train= trainset.shape[0]; num_test= testset.shape[0]; num_dev= devset.shape[0]; num_train_dev= train_dev.shape[0]
      parameters= {'ticker_stock_data':ticker_stock_data,'trainset':trainset,'testset':testset, 'devset':devset,'train_dev':train_dev,'num_train':num_train, 'num_test':num_test,'num_dev':num_dev, 'num_train_dev':num_train_dev,'ticker_name':ticker_name}
      return parameters

def convert_to_json(parameters):
    index= parameters['testset'].index
    testset=parameters['testset'][['Open','High','Low','Close','Adj Close','Volume', 'Predictions']]
    testset.loc[:,'Date']= index
    print('\ntestset.head()',testset.head())
    json_file= testset.to_json(orient='records', index=True)
    # print(json_file)
    with open('prediction_data.json', 'w') as fp:
        fp.write(json_file)
    return json_file

def get_x_y(data, N, offset):
    x, y = [], []
    for i in range(offset, len(data)):
        x.append(data[i-N:i])
        y.append(data[i])
    x = np.array(x)
    y = np.array(y)
    return x, y

def display_columns(ticker_stock_data):
  display_parameters={}
  ticker_stock_data.index= ticker_stock_data['Date']
  data= ticker_stock_data[['Open','High','Low','Close','Adj Close','Volume']]
  trainset=ticker_stock_data.loc['1990-01-01':'2010-12-31']
  devset=ticker_stock_data.loc['2011-01-01':'2015-12-31']
  testset= ticker_stock_data.loc['2016-01-01': '2019-12-31']

#   trainset=ticker_stock_data.loc['2011-01-01':'2015-12-31']
#   devset=ticker_stock_data.loc['2016-01-01': '2019-12-31']
#   dates_2020= []
#   for i in range(365):
#       dates_2020.append(datetime.date(2020, 1, 1) + datetime.timedelta(i))
#   testset= pd.DataFrame(index=dates_2020)
#   print(testset.head())
  ticker_name= ticker_stock_data['Ticker'][0]
  display_parameters={'data':data,'trainset':trainset,'devset':devset,'testset':testset,'ticker_name':ticker_name}
  return display_parameters
