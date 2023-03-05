import sys
import csv


def read_portfolio(file_name):
    'open csv containing portfolio data: symbols, prices, shares'
    portfolio = []
    with open(file_name, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        indices = [headers.index(colname) for colname in select]
        portfolio = [{colname: row[idx]
                      for colname, idx in zip(select, indices)}
                     for row in rows]

    return portfolio


def calculate_portfolio(portfolio):
    'calculate cost of a portfolio based on dict of dicts symbols: {ct, prices}'
    portfolio_value = 0.0

    for stock in portfolio:
        if 'last_price' in stock.keys():
            portfolio_value = portfolio_value + \
                (int(stock['shares']) * float(stock['last_price']))
        else:
            portfolio_value = portfolio_value + \
                (int(stock['shares']) * float(stock['price']))

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
        portfolio[idx]['last_price'] = prices[stock['name']]
    return portfolio


def make_report(portfolio):

    report = []

    for stock in portfolio:
        try:
            report.append({
                "Name": stock['name'],
                "Shares": stock['shares'],
                "Price": stock['last_price'],
                "Change": stock['last_price'] - float(stock['price'])
                }
            )
        except ValueError:
            print('Could not read', stock)
            continue

    return report


def portfolio_readout(original_value, new_value):
    if new_value < original_value:
        print('Portfolio gain/( loss ): (', new_value - original_value, ')')
    else:
        print('Portfolio gain/( loss ):', new_value - original_value)


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print()
    print(f"{headers[0]:>10}{headers[1]:>10}{headers[2]:>10}{headers[3]:>10}")
    underline = '-'*10 + ' '
    print(f"{underline*4: ^40}")
    for stock in report:
        formatted_price = f"${stock['Price']:.2f}"
        print(f"{stock['Name']: >9s}{stock['Shares']: >10} {formatted_price: >10}{stock['Change']: >10.2f}")
    return


def portfolio_report(portfolio_file_name, prices_file_name):
    portfolio = read_portfolio(portfolio_file_name)

    original_value = calculate_portfolio(portfolio)

    print('Portfolio original value:', original_value)

    prices = read_prices(prices_file_name)

    new_portfolio = update_portfolio(portfolio, prices)

    new_value = calculate_portfolio(new_portfolio)

    portfolio_readout(original_value, new_value)

    print('Portfolio current value:', new_value)

    print_report(make_report(new_portfolio))

    return


if __name__ == '__main__':
    portfolio_report(sys.argv[1], sys.argv[2])
