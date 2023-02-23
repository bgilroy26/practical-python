# pcost.py
#
# Exercise 1.27

import sys
import csv


def get_portfolio_csv_lines(file_name):
    'open csv containing portfolio data: symbols, prices, num_shares'
    portfolio = []
    with open(file_name) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                holding = dict(
                    symbol = row[0],
                    num_shares = int(row[1]),
                    price = float(row[2])
                )
                portfolio.append(holding)
            except ValueError:
                print('Could not parse', line)
                continue
        return portfolio


def calculate_cost(lines):
    'calculate cost of a portfolio based on csv input of symbols, prices, num_shares'
    portfolio_cost = 0.0

    for line in lines:
        portfolio_cost = portfolio_cost + (line['num_shares'] * line['price'])

    return portfolio_cost


file_name = sys.argv[1]

lines = get_portfolio_csv_lines(file_name)

print('Total cost:', calculate_cost(lines))
