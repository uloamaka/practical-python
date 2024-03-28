# pcost.py
#
# Exercise 3_14

import report
import sys

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s.shares * s.price for s in portfolio])

def main(argv):
    if len(sys.argv) != 1:
       raise SystemExit('Usage: %s portfile' % argv[0])
    cost = portfolio_cost(argv[1])
    return(cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)




