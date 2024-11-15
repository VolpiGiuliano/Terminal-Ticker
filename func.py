import os
import time
import yfinance as yf

def colortex(tex:str,color:str):
    '''
    Use (') for the string arguments
    '''
    palette={"red":31,"green":32,"yellow":33,"blue":34}
    out= f"\033[{palette[color]}m{tex}\033[0m"
    return out

def colornumb(numb):
    if numb<0:
        return colortex(str(round(numb,2)),'red')
    elif numb>0:
        return colortex(str(round(numb,2)),'green')
    else:
        return colortex(str(round(numb,2)),'blue')
    

def tickprint(symbols,t):
    text_to =""
    for s in symbols:
        row=(s,t.tickers[s].fast_info["lastPrice"],t.tickers[s].fast_info["lastPrice"]-t.tickers[s].fast_info["open"])
        text_to +=f"{row[0]:<10} {round(row[1],2):<10} {colornumb(row[2]):>5}\n"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\rPrices\n{text_to}",end="",flush=True)
    time.sleep(1)