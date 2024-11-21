from functions import *

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the file
file_path = os.path.join(script_dir, "portfolio.txt")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        symbols = [line.strip() for line in file]
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


t=yf.Tickers(symbols)
first_loop= True


with Live(generate_table(symbols,t), refresh_per_second=4) as live:
    while True:
        time.sleep(0.4)
        t=yf.Tickers(symbols)
        live.update(generate_table(symbols,t))