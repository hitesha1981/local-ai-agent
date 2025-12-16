import yfinance as yf

def get_stock_price(symbol: str) -> str:
    ticker = yf.Ticker(symbol)
    # Use the comprehensive .info attribute instead of .fast_info
    data = ticker.info 
     # Check if the data was successfully retrieved
    if not data:
        return f"Could not retrieve data for {symbol.upper()}. Check symbol or network connection."
    # Access keys that are consistently present in the full .info dict
    price = data.get("currentPrice", data.get("regularMarketPrice"))
    currency = data.get("currency")
    high = data.get("dayHigh", data.get("regularMarketDayHigh"))
    low = data.get("dayLow", data.get("regularMarketDayLow"))
    return (
        f"{symbol.upper()} price: {price} {currency}\n"
        f"Day High: {high}\n"
        f"Day Low: {low}"
    )