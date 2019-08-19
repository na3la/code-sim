import pandas as pd
from itertools import combinations_with_replacement
from operator import itemgetter
from tokenization import dict_builder
from hashes.new_no_hash import caller


def smap(function, arg, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(arg, args)


def __main__():
    d = dict_builder()
    breakpoint()

    test = dict(
        zip(
            sorted(combinations_with_replacement(d.keys(), 2),
                   key=itemgetter(0, 1)),
            smap(
                caller, d,
                sorted(combinations_with_replacement(d.keys(), 2),
                       key=itemgetter(0, 1)))))

    key_list = sorted(d.keys())

    ordered_lengths = []
    for x in key_list:
        temp_list = []
        for y in key_list:
            temp_list.append(test.get((x, y))) if test.get(
                (x, y)) is not None else temp_list.append(test.get((y, x)))

        ordered_lengths.append(temp_list)

    dat = pd.DataFrame(ordered_lengths, index=key_list, columns=key_list)
    dat.to_csv('TEST.csv', sep=',')


__main__()
