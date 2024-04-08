""" yf_example2.py
Example of a function to download stock prices from Yahoo Finance.
"""
import yfinance as yf

def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads stock prices from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end, ignore_tz=True)
    df.to_csv(pth)

    def add(a, b):
        """ Returns the sum of two numbers """
        return a + b

# Example
if __name__ == "__main__":
    tic = 'QAN.AX'
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    pth = 'data/qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth, start=start_date, end=end_date)
