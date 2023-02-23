# pcost.py
#
# Exercise 1.27

import sys
import csv


def get_portfolio_csv_lines(file_name):
    'open csv containing portfolio data: symbols, prices, num_shares'
    with open(file_name) as f:
        rows = csv.reader(f)
        headers = next(rows)
        return list(rows)


def calculate_cost(lines):
    'calculate cost of a portfolio based on csv input of symbols, prices, num_shares'
    portfolio_cost = 0.0

    for line in lines:
        _, num_shares, price = line
        try:
            num_shares = int(num_shares)
        except ValueError:
            print('Could not parse', line)
            continue
        try:
            price = float(price.strip())
        except ValueError:
            print('Could not parse', line)
            continue

        portfolio_cost = portfolio_cost + (num_shares * price)

    return portfolio_cost


file_name = sys.argv[1]

lines = get_portfolio_csv_lines(file_name)

print('Total cost:', calculate_cost(lines))
