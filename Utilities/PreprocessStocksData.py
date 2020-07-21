import pandas as pd 
import numpy as np
import sqlite3
from  fastai.tabular import add_datepart
from sklearn.model_selection import train_test_split


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
    add_datepart(ticker_stock_data, 'Date', drop=False)
    ticker_stock_data.drop(labels='Elapsed', axis=1,inplace=True)
    ticker_stock_data.Close.fillna(method='ffill', inplace=True)
    ticker_stock_data['Adj Close'].fillna(method='ffill', inplace=True)
    return ticker_stock_data



# def split_data(ticker_stock_data):
#       ticker_stock_data.index= ticker_stock_data['Date']
#       trainset, testset= train_test_split(ticker_stock_data, test_size=.4, random_state=1)
#       parameters={'trainset': trainset,'testset': testset,'ticker_stock_data':ticker_stock_data}
#       return parameters

def split_data(ticker_stock_data):
      ticker_stock_data.index= ticker_stock_data['Date']
      # trainset, testset= train_test_split(ticker_stock_data, test_size=.4, random_state=1)
      trainset=ticker_stock_data.loc['2010-01-01':'2018-12-31']
      testset= ticker_stock_data.loc['2019-01-01': '2019-12-31']
      ticker_name= ticker_stock_data['Ticker'][0]
      parameters={'trainset': trainset,'testset': testset,'ticker_stock_data':ticker_stock_data,'ticker_name':ticker_name}
      return parameters

def convert_to_json(parameters):
    testset=parameters['testset'][['Date','Open','High','Low','Close','Adj Close','Volume', 'Predictions']]
    json_file= testset.to_json(orient='records', index=True, lines=True)
    # # print(json_file)
    # with open('prediction_data.json', 'w') as fp:
    #     fp.write(json_file)
    return json_file


