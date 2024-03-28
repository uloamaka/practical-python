# report.py
#
# Exercise 4_4
import sys
import fileparse 
from stock import Stock

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of stock class with attribute;
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return(portfolio)

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    ''' 
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))


def make_report(portfolio, prices):
    '''Convert file into a list of tupples ('name', 'shares', 'price', 'change')'''

    report = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        report.append(summary)
    return report   

def print_report(report):
    '''print  a nicely formated table from a list of (name,shares, prices, change) tuples.'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(file1, file2):
    '''
    prints the report when the functions is called.
    '''
    portfolio = read_portfolio(file1)
    prices    = read_prices(file2)

    # Compute the current value of the portfolio
    total_value = 0.0
    for s in portfolio:
        total_value += s.shares*prices[s.name]
    # Output the report
    report = make_report(portfolio, prices)  
    print_report(report)

def main(argv):
    if len(sys.argv) != 3:
       raise SystemExit('Usage: %s portfile pricefile' % argv[0])
    report = make_report(argv[1], argv[2])
    return(report)

if __name__ == '__main__':
    import sys
    main(sys.argv)

print('God lives in me')