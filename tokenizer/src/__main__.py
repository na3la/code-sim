import time
import pandas as pd
import numpy as np
import csv
import testtokenizer as tt
from nohashkr import gst
# from karpRabinHash import krhash
from itertools import combinations
from FUKHASH import krhash


def main():

    csvfile = input("csv file name: ")
    toreadfolder = input("folder to read from: ")
    token = tt.tokenizer(toreadfolder)
    token.folderRead()
    testsrc = sorted(token.summaryDict.keys())
    fi = list(testsrc)[0]
    iff = list(testsrc)[1]
    labs = []
    pat = []
    c1 = []
    c2 = []
    c3 = []
    featurevec = []

    mmarr = []
    c2 = []  # do same as mmarr for len(gs.matchlist.values())
    c3 = []

    for x, y in enumerate(testsrc):

        mmarr.append([])
        c2.append([])
        c3.append([])

        for z in testsrc:
            gs = gst(token.summaryDict[z][0], token.summaryDict[y][0], 10)
            gs.scanPattern()
            gs.gprop()

            if not len(gs.matchlist.keys()) or y == z:
                mmarr[x].append(0)
                c2[x].append(0)
                c3[x].append(0)
                continue
            mmarr[x].append(1 / (max(gs.matchlist.keys())))
            c2[x].append(len(gs.matchlist.values()))

            if not gs.gen_prop:
                c3[x].append(0)
                continue
            prop_match_btw_files = abs(
                gs.length_of_tokens_tiled * 2 /
                (len(token.summaryDict[z][0]) + len(token.summaryDict[y][0])) -
                1)
            # prop_match_btw_files = (len(token.summaryDict[z][0]) +
            #                        len(token.summaryDict[y][0]) /
            #                        (gs.length_of_tokens_tiled * 2)) - 1

    #       c3[x].append(prop_match_btw_files)

    dat = pd.DataFrame(mmarr, index=list(testsrc), columns=list(testsrc))
    dat.to_csv(csvfile + ".csv", sep=',')
    # dat3 = pd.DataFrame(c3, index=list(testsrc), columns=list(testsrc))
    # dat3.to_csv(csvfile + "3.csv", sep=',')


main()
