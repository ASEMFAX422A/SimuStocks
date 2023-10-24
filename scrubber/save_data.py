# save_data.py

def save_data(price, ticker):
    file_name = f"{ticker}_stock_prices.txt"
    with open(file_name, 'a') as f:
        f.write(f"{price}\n")

