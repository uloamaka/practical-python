# report.py
#
# Exercise 4_4
import sys
import fileparse 
from stock import Stock
import tableformat 

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
    '''
    Convert file into a list of tupples ('name', 'shares', 'price', 'change')
    '''
    report = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        report.append(summary)
    return report   

def print_report(report, formatter):
    '''
    print  a nicely formated table from a list of (name,shares, prices, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(file1, file2, fmt='txt'):
    '''
    prints the report when the functions is called.
    '''
    portfolio = read_portfolio(file1)
    prices    = read_prices(file2)

    # Create the report data
    report = make_report(portfolio, prices)  

    # Output the report
    formatter = tableformat.create_formatter(fmt)    
    print_report(report, formatter)

def main(argv):
    if len(sys.argv) != 3:
       raise SystemExit('Usage: %s portfile pricefile' % argv[0])
    report = make_report(argv[1], argv[2])
    return(report)

if __name__ == '__main__':
    import sys
    main(sys.argv)

print('God lives in me')