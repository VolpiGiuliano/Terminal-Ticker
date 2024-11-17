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


while True:
    if first_loop:
        table=data_request(first_loop,symbols,t)
        first_loop=False
    table=data_request(first_loop,symbols,t)
    df = pd.DataFrame(table)
    print_table_in_place(df)
    time.sleep(0.7)