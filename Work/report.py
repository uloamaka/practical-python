# report.py
#
# Exercise 3_12
import csv
import fileparse 

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))


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