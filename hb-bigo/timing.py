#### eprint
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.stderr.flush()
#### end eprint

def time(code, symbols=None, namespace='__main__'):
    import timeit
    if symbols:
        setup = 'from %s import %s' % (namespace,
            ', '.join(symbols))
    else:
        setup = ''

    eprint('Running: %s' % code)
    return timeit.timeit(code, setup=setup, number=100000)

def time_multiple(code, n_list, sym=None, ns='__main__'):
    times = {}
    for n in n_list:
        times[n] = time((code % n), sym, ns)
    return times
