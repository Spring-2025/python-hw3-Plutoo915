import yfinance as yf
import pandas as pd

def get_stock_data(symbol):
    data = yf.download(symbol) 
    prices = data['Close']
    return prices

def get_returns(pricevec):
    n = len(pricevec)
    ratiovec = pricevec[1:n] / pricevec[:n-1]
    returns = ratiovec - 1 
    return returns

def YahooData2returns(YahooData):
   if isinstance(YahooData, pd.DataFrame):  
        prices = YahooData['Adj Close']  
    else:
        prices = get_stock_data(YahooData)  
    pricevec = prices.values  
    returns = get_returns(pricevec)
    return returns
