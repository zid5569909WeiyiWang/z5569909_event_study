"""
yf_example3.py
This module is for download the stock price of Qantas and save as CSV file.
"""

import os
from yf_example2 import yf_prc_to_csv

data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def qan_prc_to_csv(year):
    """
    Downloads Qantas stock prices for a given year and saves them in a CSV file.

    Parameters:
    year (int): The year for which to download stock prices.
    """
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    file_name = f"qan_prc_{year}.csv"
    path = os.path.join(data_folder, file_name)

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    yf_prc_to_csv('QAN.AX', path, start=start_date, end=end_date)

if __name__ == "__main__":
    qan_prc_to_csv(2020)
