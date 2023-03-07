# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=[], types=[], has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv into a list of records
    '''
    records = []

    if select and not has_headers:
        raise RuntimeError('"select" argument requires column headers')

    if isinstance(filename, str):
        f = open(filename, 'rt')
        rows = csv.reader(f, delimiter=delimiter)
        rows = iter([row for row in rows])
        f.close()
    else:
        rows = iter([row.split(',') for row in filename])

    # read the file headers
    if has_headers:
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            names = [headers[index].strip() for index in indices]

            for idx, row in enumerate(rows):
                if not row:
                    continue

                if types:
                    try:
                        record = { name.strip(): ty(row[index]) for name, index, ty in
                                zip(names, indices, types) }
                    except ValueError as e:
                        if silence_errors:
                            continue
                        print('Row', str(idx) + ': Could not convert')
                        print('Row', str(idx) + ':', e)
                        continue
                else:
                    record = { name.strip(): row[index] for name, index in
                            zip(names, indices) }
                records.append(record)
        else:
            for idx, row in enumerate(rows):
                if not row:
                    continue

                if types:
                    record = {}
                    for header, ty, item in zip(headers, types, row):
                        try:
                            record[header.strip()] = ty(item)
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
                    record = tuple(ty(item) for ty, item in zip(types, row))
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
