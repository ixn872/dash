import yfinance as yahooFinance


def get_weekly(instrument):
    SYM = yahooFinance.Ticker(instrument)
    sym = SYM.history(period="max")

    logic = {'Open'  : 'first',
             'High'  : 'max',
             'Low'   : 'min',
             'Close' : 'last',
             'Volume': 'sum'}

    weekly  = sym.resample('W-Fri',).apply(logic).reset_index()
    
    sym = sym.reset_index()[['Date','Open','High','Low','Close','Volume']]
        
    return weekly
