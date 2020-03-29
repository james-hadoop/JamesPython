import itertools
import functools


def groupby1(arr, func=lambda x: x, filter_=lambda x: True):
    def groupby2(arr):
        arr = sorted(arr, key=lambda x: x[0])
        for k, g in itertools.groupby(arr, lambda x: x[0]):
            yield [k, [x[1] for x in g]]

    res = map1(lambda x: [x[0], func(x[1])] if filter_(x[1]) else None, groupby2(arr))
    return filter1(lambda x: x is not None, res)


def map1(lam, *args):  # functional programming
    return list(map(lam, *args))


def filter1(lam, *args):  # functional programming
    return list(filter(lam, *args))


def reduce1(f, _list):  # functional programming
    return functools.reduce(f, _list)
