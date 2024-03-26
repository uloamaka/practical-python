# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select is not None or has_headers == False:
        raise RuntimeError('select argument requires column headers')
    with open(filename) as f: 
        rows = csv.reader(f, delimiter=delimiter)
        # Read the file headers (if any)
        headers = next(rows) if has_headers else []
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []    
        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:     # Skip rows with no data
                continue
            if select:
            # if a type was given, convert the returned data by the given type
                row = [ row[index] for index in indices]
            # Apply type conversion to the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        return records


    
