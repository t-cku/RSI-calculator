from flask import Flask, render_template, request
from datetime import date
from rsicalc import fetch_data, calc_rsi, plot_rsi, plot_price
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    current_date = f"{day}-{month}-{year}"
    #check if user submitted the form with a stock symbol
    if request.method == 'POST':
        ticker = request.form['ticker']  #pulls the value from form input
        ticker = ticker.upper()  #turn into uppercase
        

        print("POST received", ticker)

        try:
            data = fetch_data(ticker)

            rsi = calc_rsi(data)

            latest_price = round(data['Close'].iloc[-1], 2)
            latest_rsi = round(rsi.iloc[-1], 2)

            print("RSI is calculated")
            plot_price(data, ticker)
            plot_rsi(data, rsi, ticker)

            #this function is a void one
            #saves the RSI chart image to the static folder
            return render_template('index.html',
                                   ticker=ticker,
                                   rsi=rsi,
                                   image_price=f'/static/{ticker}_price.png',
                                   image_rsi=f'/static/{ticker}_rsi.png',
                                   current_price=latest_price,
                                   current_rsi=latest_rsi,
                                    current_date = current_date)

        except Exception as e:
            #error
            return render_template('index.html', error=str(e), current_date = current_date)

    print("Route is working!")
    return render_template('index.html', current_date=current_date)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
