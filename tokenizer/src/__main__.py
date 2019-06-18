import time
import testtokenizer as tt
from nohashkr import gst
from karpRabinHash import krhash
from itertools import combinations


def main():
    token = tt.tokenizer('../javahw1/fixed')
    token.folderRead()
    testsrc = token.summaryDict.keys()
    fi = list(testsrc)[0]
    iff = list(testsrc)[1]

    print("hash")
    startt = time.perf_counter_ns()
    for x in list(combinations(testsrc, 2)):
        gs = krhash(token.summaryDict[x[0]][0], token.summaryDict[x[1]][0],
                    2)
        gs.genHashTbl()

    print(time.perf_counter_ns() - startt)

    print("no hash")
    startt = time.perf_counter_ns()
    for x in list(combinations(testsrc, 2)):
        gs = gst(token.summaryDict[x[0]][0], token.summaryDict[x[1]][0], 2)
        gs.scanPattern()

    print(time.perf_counter_ns() - startt)


main()
