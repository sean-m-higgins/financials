import yfinance as yf
import pandas as pd 
import pandas_datareader.data as web
import datetime

# ------------------------------------------------------------------------------------------
# SOURCE: https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Historical data example:

# #define the ticker symbol
# tickerSymbol = 'MSFT'

# #get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)

# #get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# #see your data
# print(tickerDf)
# print(tickerData.info)



# ------------------------------------------------------------------------------------------
# SOURCE: https://medium.com/@cjriggio3/historical-stock-data-and-basic-analysis-for-python-users-f1beb4e9170b
# Historical Stock Data and Basic Analysis:

#Define a start and end date for the data you want to pull
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2019, 5, 31)

df_500 = web.DataReader('^GSPC', 'yahoo', start, end)
df_500 = df_500.reset_index()
print(df_500.tail())

# Basic Analysis:

# True Range - measures market volatility
# ... = ( max( today's high or yeterday's close ) - min( today's low or yesterday's close ) )
# ... usually average over a 14 day window to get a more contextual representation 
# .... good window sizes -> 3, 7, 14 days





# ------------------------------------------------------------------------------------------
# SOURCE: https://learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/
# ...