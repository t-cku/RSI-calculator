import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt 
import os

def fetch_data(ticker):
    data = yf.Ticker(ticker).history(period='1y', interval='1d') 

    return data 

def calc_rsi(data, period = 14):
    #delta means the difference betw the closing prices of consecutive days
    delta = data['Close'].diff()
    #gain is the +ve change in price, loss is the -ve change in price
    gain = delta.clip(lower=0)
    #if value is less than 0, it is replaced with 0. else value remains same
    loss = -delta.clip(upper=0)

    #calculate avg gain and loss using a ROLLING mean
    #.mean() is a pandas method that calc the mean of a series

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    #relative strength RS = avg gain / avg loss
    rs = avg_gain / avg_loss

    #calculate RSI = 100 - (100 / (1 + RS))
    rsi = 100 - (100 / (1 + rs))
    return rsi

def plot_rsi(data, rsi, ticker):
    data['rsi'] = rsi
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['rsi'], label='RSI', color='blue')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f'RSI for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(f'static/{ticker}_rsi.png')
    plt.close()


def plot_price(data, ticker):
    
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.title(f'Close Price for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'static/{ticker}_price.png')
    plt.close()