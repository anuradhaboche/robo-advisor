import bs4 as bs
import requests
import pandas as pd
from pymongo import MongoClient
import datetime
from pandas_datareader import data as pdr
import yfinance as yf


def scrap_ticker_data():
    response= requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup= bs.BeautifulSoup(response.text, 'html.parser')
    table= soup.find('table', {'class': 'wikitable sortable'})

    tickers =[]
    companies=[]

    for row in table.findAll('tr')[1:]:
        ticker= row.findAll('td')[0].text
        company= row.findAll('td')[1].text
        tickers.append(ticker)
        companies.append(company)

    tickers=[ticker.strip() for ticker in tickers]
    dictionary={'ticker':tickers, 'company_name':companies}
    ticker_data= pd.DataFrame(dictionary)

    return ticker_data

def store_ticker_data(ticker_data):
    client= MongoClient()
    database= client['portfolio_db']
    collection= database['tickers']
    ticker_data.reset_index(inplace=True)
    dictionary = ticker_data.to_dict("records")
    collection.insert_many(dictionary)
    # print(list(database.tickers.find({})))

    return

def scrape_store_stocks_data():
    yf.pdr_override() 
    client= MongoClient()
    database= client['portfolio_db']
    collection= database['stocks_data']

    start_date = datetime.datetime(1990,1,1)
    end_date = datetime.datetime(2019,12,31)
    # tickers=['GOOG','IBM', 'YELP']
    tickers=scrap_ticker_data()
    tickers=tickers['ticker']

    for ticker in tickers:
        try:
            data= pdr.get_data_yahoo(ticker, start_date, end_date)
        except:
            data= pdr.DataReader(ticker,'google', start_date, end_date)
    
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")
        collection.insert_one({"index":ticker,"data":data_dict})

    return

def get_stocks_data():
    client= MongoClient()
    database= client['portfolio_db']
    collection= database['stocks_data']
    data_from_db = collection.find_one({"index":"GOOG"})
    output_dataframe = pd.DataFrame(data_from_db["data"])
    output_dataframe.set_index("Date",inplace=True)
    print(output_dataframe)

    return