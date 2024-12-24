import os
import time
import yfinance as yf
from rich.live import Live
from rich.table import Table


def textreader(file_name:str):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the file
    file_path = os.path.join(script_dir, file_name)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            symbols = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return symbols


def generate_table(tickers,t) -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("Tickers", justify="left", style="cyan", no_wrap=True)
    table.add_column("Price", justify="left", style="cyan", no_wrap=True)
    table.add_column("PL", justify="left", style="cyan", no_wrap=True)
    table.add_column("Currency", justify="left", style="cyan", no_wrap=True)
    table.add_column("Type", justify="left", style="cyan", no_wrap=True)

    for _,symbol in enumerate(tickers):
        try:
            asset=t.tickers[symbol].fast_info
            pl= round(asset["lastPrice"]-asset["open"],2)
            table.add_row(
                #f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
                f"{symbol}",
                f"{round(asset['lastPrice'],2)}",
                f"[red]{pl}"if pl<0 else f"[green]{pl}",
                asset["currency"],
                asset["quoteType"]
            )
        except KeyError:
            table.add_row(
                #f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
                f"{symbol}",
                f"KeyError",
                f"KeyError",
                f"KeyError",
                f"KeyError"
            )
    return table

def main():
    symbols= textreader('portfolio.txt')
    t=yf.Tickers(symbols)
    first_loop= True

    try:

        with Live(generate_table(symbols,t), refresh_per_second=4) as live:
            while True:
                time.sleep(0.4)
                t=yf.Tickers(symbols)
                live.update(generate_table(symbols,t))
    except KeyboardInterrupt:
        print("GOODBYE!")