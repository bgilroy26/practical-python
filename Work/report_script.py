import sys
import fileparse


def read_portfolio(file_name):
    'open csv containing portfolio data: symbols, prices, shares'
    portfolio = fileparse.parse_csv(file_name,
                                    select=['name', 'shares', 'price'],
                                    types=[str, int, float]
                                    )
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
    'open csv containing price data: name, price'
    prices = fileparse.parse_csv(file_name,
                                 types=[str, float],
                                 has_headers=False
                                 )
    return prices


def get_price_of_stock(prices, symbol):
    return [price for price in prices if price[0] == symbol][0]


def update_portfolio(portfolio, prices):

    for idx, stock in enumerate(portfolio):
        portfolio[idx]['last_price'] = \
            get_price_of_stock(prices, portfolio[idx]['name'])[1]
    return portfolio


def make_report(portfolio):

    report = []

    for stock in portfolio:
        try:
            report.append({
                "Name": stock['name'],
                "Shares": stock['shares'],
                "Price": stock['price'],
                "Change": stock['price'] - float(stock['last_price'])
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


def main(portfolio_file_name, prices_file_name):
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
    main(sys.argv[1], sys.argv[2])
