# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=[]):
    '''
    Parse a csv into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # read the file headers
        headers = next(rows)
        records = []

        if select == []:
            for row in rows:
                if not row:
                    continue
                record = dict(zip(headers, row))
                records.append(record)
        else:
            indices = [headers.index(colname) for colname in select]
            names = [headers[index] for index in indices]
            for row in rows:
                record = { name: row[index] for name, index in zip(names, indices) }
                records.append(record)

    return records
