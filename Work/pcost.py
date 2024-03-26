# pcost.py
#
# Exercise 1.27
# total_cost = 0.0

# with open('./Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         total_cost += float(row[2]) * int(row[1])

# print('Total Cost', total_cost )


# def portfolio_cost(filename):
    # total_cost = 0.0
    # with open(filename, 'rt') as f:
    #     next(f)
    #     for line in enumerate(f):
    #         total_cost = line
    #         # row = line.split(',')
    #         # total_cost += float(row[2]) * int(row[1])
    # return total_cost
import csv

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows) 
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost    



# cost = portfolio_cost('Data/missing.csv')
# cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost:', cost)