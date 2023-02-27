# pcost.py
#
# Exercise 1.27

import sys
import csv


def calculate_cost(file_name):
    'calculate cost of a portfolio based on csv input of symbols, prices, num_shares'
    portfolio_cost = 0.0
    portfolio = []

    with open(file_name) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = dict(zip(headers, row))
            portfolio.append(stock)

        for idx, stock in enumerate(portfolio):
            try:
                num_shares = int(stock['shares'])
                price = float(stock['price'])
            except ValueError:
                print('Row ' + idx + ': Could not parse', line)
                continue

            portfolio_cost = portfolio_cost + (num_shares * price)

    return portfolio_cost


file_name = sys.argv[1]

print('Total cost:', calculate_cost(file_name))
