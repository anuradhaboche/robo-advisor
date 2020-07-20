import bs4 as bs
import requests
import pandas as pd
from pymongo import MongoClient
import datetime
from pandas_datareader import data as pdr
import yfinance as yf
import sqlite3

def scrape_ticker_data():
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

def store_ticker_data():
    ticker_data= scrape_ticker_data()
    connection = sqlite3.connect('/Users/anuradha/Desktop/Database/portfolio_db.db')
    connection.execute('create table ticke_data( ticker_name varchar(10), company_name TEXT)')
    ticker_data.reset_index(inplace=True)
    ticker_data.to_sql('ticker_data', connection,if_exists='append',index=False)

    return

def scrape_store_stocks_data():
    connection = sqlite3.connect('/Users/anuradha/Desktop/Database/portfolio_db.db')
    # connection.execute('create table stocks_data( ticker_name varchar(10), Date INTEGER, AdjClose REAL)')
    yf.pdr_override() 
    start_date = datetime.datetime(1990,1,1)
    end_date = datetime.datetime(2019,12,31)
    tickers=scrape_ticker_data()
    tickers=tickers['ticker']
    for ticker in tickers:
        data= pdr.get_data_yahoo(ticker, start_date, end_date)
        data['Ticker']=ticker
        data.reset_index(inplace=True)
        data.to_sql('stocks_data',connection,if_exists='append',index=False)
    return

