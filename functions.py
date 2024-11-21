import os
import time
import yfinance as yf
from rich.live import Live
from rich.table import Table



def generate_table(tickers,t) -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("Tickers", justify="left", style="cyan", no_wrap=True)
    table.add_column("Price", justify="left", style="cyan", no_wrap=True)
    table.add_column("PL", justify="left", style="cyan", no_wrap=True)
    table.add_column("Currency", justify="left", style="cyan", no_wrap=True)
    table.add_column("Type", justify="left", style="cyan", no_wrap=True)

    for _,symbol in enumerate(tickers):
        asset=t.tickers[symbol].fast_info
        pl= round(asset["lastPrice"]-asset["open"],2)
        table.add_row(
            #f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
            f"{symbol}",f"{round(asset['lastPrice'],2)}",
            f"[red]{pl}"if pl<0 else f"[green]{pl}",
            asset["currency"],
            asset["quoteType"]
        )
    return table
