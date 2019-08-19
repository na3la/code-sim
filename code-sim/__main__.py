import pandas as pd
from tokenization import dict_builder
from hashes.nohashkr import gst
from hashes.gb_test_hash import greedy_string_tiling
from _diff_lib_util import return_ratio
#from tokenizationC import dict_builder
from gst.new_kr import take_text_pattern


def main():

    d = dict_builder()
    raw_dict = d[1]
    token_dict = d[0]
    fileuuids = sorted(token_dict.keys())

    mmarr = []
    c2 = []  # do same as mmarr for len(gs.matchlist.values())
    c3 = []

    for x, y in enumerate(fileuuids):

        mmarr.append([])
        c2.append([])
        c3.append([])

        for z in fileuuids:
#            if y == '747976' or z == '747976':
#                breakpoint()
            n = take_text_pattern(token_dict.get(z), token_dict.get(y), 1)
            gs = gst(token_dict.get(y), token_dict.get(z), 1)
            gs.scanPattern()
            l = greedy_string_tiling(token_dict.get(y), token_dict.get(z))
            if l != gs.length_of_tokens_tiled != n:
                print(n)
                print(gs.length_of_tokens_tiled)
                print(l)
                breakpoint()
            c2[x].append(abs(return_ratio(raw_dict.get(y), raw_dict.get(z))-1))

            if not len(gs.matchlist.keys()):
#                c2[x].append(0)
                c3[x].append(0)
                continue
            elif token_dict.get(y) == token_dict.get(z) or y == z:
                mmarr[x].append(0)
#                c2[x].append(100)
                c3[x].append(0)
                continue

            if gs.length_of_tokens_tiled == 0:
                breakpoint()
            ratio = (len(token_dict.get(y)) + len(token_dict.get(z)) / 2)
            mmarr[x].append(
                abs(((gs.length_of_tokens_tiled * 2) /
                     (len(token_dict.get(y)) + len(token_dict.get(z)))) - 1))
            c3[x].append((ratio / gs.length_of_tokens_tiled) - 1)

#    dat = pd.DataFrame(mmarr, index=list(fileuuids), columns=list(fileuuids))
#    dat.to_csv("C_token1" + ".csv", sep=',')
#    dat3 = pd.DataFrame(c3, index=list(fileuuids), columns=list(fileuuids))
#    dat3.to_csv("C_token2" + ".csv", sep=',')
#    dat2 = pd.DataFrame(c2, index=list(fileuuids), columns=list(fileuuids))
#    dat2.to_csv("C_diff_ratio", sep=',')


main()
