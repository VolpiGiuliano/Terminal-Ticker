import os
import time
import yfinance as yf
from tabulate import tabulate
from colorama import Fore, Style
import pandas as pd

data= {
    
    "tickers":[],
    "price":[],
    "pl":[],
    "currency":[],
    "type":[]       
}


def data_request(first_loop:bool,symbols:list,t):

    if first_loop:
        for s in symbols:
            asset=t.tickers[s].fast_info
            data["tickers"].append(s)
            data["price"].append(asset["lastPrice"])
            data["pl"].append(asset["lastPrice"]-asset["open"])
            data["currency"].append(asset["currency"])
            data["type"].append(asset["quoteType"])

        return data
    
    elif first_loop==False:
        for i, s in enumerate(symbols):
            asset=t.tickers[s].fast_info

            if data["type"][i] =="CURRENCY":
                data["price"][i]= round(asset["lastPrice"],7)
                data["pl"][i]= round(asset["lastPrice"] - asset["open"],7)
            else:
                data["price"][i]= round(asset["lastPrice"],2)
                data["pl"][i]= round(asset["lastPrice"] - asset["open"],2)
        return data


def print_table_in_place(df):
    colored_df = df.apply(colorize_row, axis=1)
    table = tabulate(colored_df, headers="keys", tablefmt="rounded_grid",showindex=False,stralign="left")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
    print(table)

def colorize_row(row):
    row['pl'] = f"{Fore.GREEN}{row['pl']}{Style.RESET_ALL}" if row['pl'] >= 0 else f"{Fore.RED}{row['pl']}{Style.RESET_ALL}" 
    return row
