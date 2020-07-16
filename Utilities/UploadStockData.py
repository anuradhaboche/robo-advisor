
import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
from ScrapData import scrap_ticker_data, store_ticker_data,scrape_store_stocks_data,get_stocks_data
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# ticker_data=scrap_ticker_data()
# store_ticker_data(ticker_data)
scrape_store_stocks_data()
# dataframe=get_stocks_data()
# print(dataframe.hist())