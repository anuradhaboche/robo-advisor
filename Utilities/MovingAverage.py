import pandas as pd
import numpy as np
from ScrapData import get_stocks_data
import matplotlib.pyplot as plt
from pymongo import MongoClient

stocks_data= get_stocks_data()
print(stocks_data.head())



