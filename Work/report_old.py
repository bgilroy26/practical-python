# pcost.py
#
# Exercise 1.27

import sys
import csv
import collections


def read_portfolio(file_name):
    'open csv containing portfolio data: symbols, prices, shares'
    portfolio = []
    with open(file_name, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:

            try:
                stock = {
                    'symbol' : row[0],
                    'shares' : int(row[1]),
                    'initial_price' : float(row[2])
                }
            except ValueError:
                print('Could not parse', row)
                continue

            portfolio.append(stock)
    return portfolio


def calculate_portfolio(portfolio):
    'calculate cost of a portfolio based on dict of dicts symbols: {ct, prices}'
    portfolio_value = 0.0

    for stock in portfolio:
        portfolio_value = portfolio_value + \
            (stock['shares'] * stock['initial_price'])

    return portfolio_value


def read_prices(file_name):
    'open csv containing price data: symbol, price'
    prices = {}
    with open(file_name, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                try:
                    prices[row[0]] = float(row[1])
                except ValueError:
                    print('Could not parse', row)
                    continue
            else:
                continue
    return prices


def update_portfolio(portfolio, prices):

    for idx, stock in enumerate(portfolio):
        if stock['symbol'] in prices.keys():
            portfolio[idx]['current_price'] = prices[stock['symbol']]
    return portfolio


def make_report(portfolio, prices):

    report = []

    Stock = collections.namedtuple(
        'Stock',
        ['Name', 'Shares', 'Price', 'Change']
    )

    aug_portfolio = update_portfolio(portfolio, prices)

    for stock in aug_portfolio:
        report.append(Stock(stock['symbol'],
                            stock['shares'],
                            stock['current_price'],
                            stock['current_price'] - stock['initial_price']
                            )
                      )
    return report


def main():
    portfolio_file_name = sys.argv[1]

    portfolio = read_portfolio(portfolio_file_name)

    original_value = calculate_portfolio(portfolio)

    print('Portfolio original value:', original_value)

    prices_file_name = sys.argv[2]

    prices = read_prices(prices_file_name)

    new_portfolio = update_portfolio(portfolio, prices)

    new_value = calculate_portfolio(new_portfolio)

    print('Portfolio current value:', new_value)

    if new_value < original_value:
        print('Portfolio gain/( loss ): (', new_value - original_value, ')')
    else:
        print('Portfolio gain/( loss ):', new_value - original_value)

    return


if __name__ == '__main__':
    main()
