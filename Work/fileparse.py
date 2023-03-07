# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=[], types=[], has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError('"select" argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []

        # read the file headers
        if has_headers:
            headers = next(rows)

            if select:
                indices = [headers.index(colname) for colname in select]
                names = [headers[index] for index in indices]

                for idx, row in enumerate(rows):
                    if not row:
                        continue

                    if types:
                        try:
                            record = { name: type(row[index]) for name, index, type in
                                    zip(names, indices, types) }
                        except ValueError as e:
                            if silence_errors:
                                continue
                            print('Row', str(idx) + ': Could not convert')
                            print('Row', str(idx) + ':', e)
                            continue
                    else:
                        record = { name: row[index] for name, index in
                                zip(names, indices) }
                    records.append(record)
            else:
                for idx, row in enumerate(rows):
                    if not row:
                        continue

                    if types:
                        record = {}
                        for header, type, item in zip(headers, types, row):
                            try:
                                record[header] = type(item)
                            except ValueError as e:
                                if silence_errors:
                                    continue
                                print('Row', str(idx) + ': Could not convert')
                                print('Row', str(idx) + ':', e)
                                continue
                    else:
                        record = dict(zip(headers, row))
                    records.append(record)

        else:
            for idx, row in enumerate(rows):
                if not row:
                    continue

                if types:
                    try:
                        record = tuple(type(item) for type, item in zip(types, row))
                    except ValueError as e:
                        if silence_errors:
                            continue
                        print('Row', str(idx) + ': Could not convert')
                        print('Row', str(idx) + ':', e)
                        continue
                else:
                    record = tuple(row)
                records.append(record)

    return records
