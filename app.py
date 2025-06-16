from flask import Flask, render_template, request 

from rsicalc import fetch_data, calc_rsi, plot_rsi
import os

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    #check if user submitted the form with a stock symbol
    if request.method == 'POST':
        ticker = request.form['ticker'] #pulls the value from form input
        ticker = ticker.upper() #turn into uppercase

        print("POST received", ticker)

        try:
            data = fetch_data(ticker)

            rsi = calc_rsi(data)
            print("RSI is calculated")

            plot_rsi(data, rsi, ticker)
            #this function is a void one 
            #saves the RSI chart image to the static folder
            return render_template('index.html', ticker=ticker, rsi = rsi, image_path=f'/static/{ticker}_rsi.png')

        except Exception as e:
            #error
            return render_template('index.html', error=str(e))

    print("Route is working!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


