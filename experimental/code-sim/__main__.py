import pandas as pd
from tokenizer.src import src as tt
from tokenization import dict_builder
from hashes.nohashkr import gst
from lib.main._option import _option
# from karpRabinHash import krhash


def main():

    #csvfile = "FULLWORDADJFULLCHECK"
    # token = tt.tokenizer(_option())
    # token.folderRead()
    # testsrc = sorted(token.summaryDict.keys())
    d = dict_builder()
    fileuuids = sorted(d.keys())

    mmarr = []
    c2 = []  # do same as mmarr for len(gs.matchlist.values())
    c3 = []

    for x, y in enumerate(fileuuids):

        mmarr.append([])
        c2.append([])
        c3.append([])

        for z in fileuuids:
            gs = gst(d.get(y), d.get(z), 1)
            gs.scanPattern()
            gs.gprop()

            if not len(gs.matchlist.keys()):
                # mmarr[x].append(0)
                c2[x].append(0)
                c3[x].append(0)
                continue
            elif d.get(y) == d.get(z) or y == z:
                mmarr[x].append(0)
                c2[x].append(100)
                c3[x].append(0)
                continue

            if gs.length_of_tokens_tiled == 0:
                breakpoint()
            ratio = (len(d.get(y)) + len(d.get(z)) / 2)
            mmarr[x].append(
                abs(((gs.length_of_tokens_tiled * 2) /
                     (len(d.get(y)) + len(d.get(z)))) - 1))
            c2[x].append(len(gs.matchlist.values()))
            c3[x].append((ratio / gs.length_of_tokens_tiled) - 1)


#    sizedcount = progtot/progcount
#    for x in c3:
#        for y in range(len(x)):
#            if not x[y]:
#                continue
#            x[y] = (sizedcount/x[y])-1
    dat = pd.DataFrame(mmarr, index=list(fileuuids), columns=list(fileuuids))
    dat.to_csv("token_ltt_ldd" + ".csv", sep=',')
    dat3 = pd.DataFrame(c3, index=list(fileuuids), columns=list(fileuuids))
    dat3.to_csv("token_avg_ltt" + ".csv", sep=',')
    #dat2 = pd.DataFrame(c2, index=list(fileuuids), columns=list(fileuuids))
    #dat2.to_csv("unadjmatchlist.csv", sep=',')

main()
