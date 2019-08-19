import hacking as hk
import testtokenizer as tk
from itertools import starmap
from itertools import combinations_with_replacement
from operator import itemgetter


def _gen_data(tokens, uuid1, uuid2):
    return tuple((uuid1, uuid2, tokens[uuid1][0], tokens[uuid1][1],
                  tokens[uuid2][0], tokens[uuid2][1]))


def _code_match_poc(data):
    # POC: data[0]-data[3] --> token_vec_1, raw_vec_1, token_vec_2, raw_vec_2
    k = tuple(data)
    # for tup in k:
    #    print('\n uuid1 ' + str(tup[0]) + '\n uuid2 ' + str(tup[1]) +
    #          '\n tok_1 ' + tup[2] + '\n raw_1 ' + tup[3] + ' \n tok_2 ' +
    #          tup[4] + ' \n raw_2 ' + tup[5])
    for st in starmap(
            lambda ar1, ar2, ar3, ar4, ar5, ar6:
            str('\n uuid1 ' + str(ar1) + '\n uuid2 ' + str(
                ar2) + '\n tok_1 ' + ar3 + '\n raw_1 ' + ar4 + ' \n tok_2 ' +
                ar5 + ' \n raw_2 ' + ar6), k):
        print(st)


def starrmap(function, arg, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(arg, *args)


def __main__():

    # input(">> source file folder? ")
    src_folder = "/home/anon/notebooks/code-sim/tokenizer/javahw1/newfixed/"

    token = tk.tokenizer(src_folder)
    token.folderRead()

    _code_match_poc(
        starrmap(
            _gen_data, token.summaryDict,
            sorted(combinations_with_replacement(token.summaryDict.keys(), 2),
                   key=itemgetter(0, 1))))


if __name__ == '__main__':
    __main__()
