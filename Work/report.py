# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

    return portfolio


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


def make_report(portfolio, prices):
    '''Convert file into a list of tupples ('name', 'shares', 'price', 'change')'''

    report = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)
    return report   


def print_report(report):
    '''
    prints the report when the functions is called.
    '''
    portfolio = read_portfolio('Data/portfoliodate.csv')
    prices    = read_prices('Data/prices.csv')

    # Calculate the total cost of the portfolio
    total_cost = 0.0
    for s in portfolio:
        total_cost += s['shares']*s['price']
    print('Total cost', total_cost)

    # Compute the current value of the portfolio
    total_value = 0.0
    for s in portfolio:
        total_value += s['shares']*prices[s['name']]
    print('Current value', total_value)
    print('Gain', total_value - total_cost)
    # Output the report
    report = make_report(portfolio, prices)  

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)
    return row



print('God lives in me')