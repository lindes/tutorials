def slurp(filename):
    import csv
    reader = csv.reader(open(filename, 'r'))

    header = reader.next()
    for i in range(1,len(header)):
        header[i] = int(header[i])
    rows = list(reader)

    data = {}
    names = []
    for row in rows:
        names.append(row[0])
        data[row[0]] = [float(col) for col in row[1:]]
    return { 'title'   : header[0],
             'n_values': header[1:],
             'names'   : names,
             'data'    : data,
           }

    return data

def dump(data, filename, order = None):
    '''A function to take data in a particular form,
and output it to a CSV file of the specified filename.'''

    import csv
    writer = csv.writer(open(filename, 'wb'))
    # the keys from an arbitrary item are the n values:
    n_values = sorted(data[data.keys()[0]])

    # write it all out:
    writer.writerow(['method'] + n_values)
    if order:
        methods = order
    else:
        methods = data.keys()
    for key in methods:
        values = data[key]
        writer.writerow([key] +
            map((lambda k: values[k]), n_values))
