# pcost.py
#
# Exercise 1.27

import sys
import report


def calculate_cost(file_name):
    'calculate cost of a portfolio based on csv input of symbols, prices, num_shares'
    portfolio_cost = 0.0

    portfolio = report.read_portfolio(file_name)

    for idx, stock in enumerate(portfolio):
        num_shares = int(stock['shares'])

        try:
            price = float(stock['initial_price'])
        except KeyError:
            price = float(stock['price'])

        portfolio_cost = portfolio_cost + (num_shares * price)

    return portfolio_cost


def main(args):
    print('Total cost:', calculate_cost(args[1]))
    return


if __name__ == '__main__':
    main(sys.argv)
