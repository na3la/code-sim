"""
karp-rabin-hash algorithm implementation of greedy tiling


"""

# TODO make mask function
# TODO test..

import numpy as np
from collections import deque, OrderedDict


class krhash():
    def __init__(self, itext, pattern, s):
        self.mml = OrderedDict()
        self.hashtable = dict()
        self.inputText = list(itext)
        self.pattern = list(pattern)
        self.tmask = [0] * len(self.inputText)
        self.pmask = [0] * len(self.pattern)
        self.s = s

    def maskArray(self, p, t, maxmatch):

        for i in range(maxmatch):
            if self.tmask[t + i] != 1:
                self.tmask[t + i] = 1

            if self.pmask[p + i] != 1:
                self.pmask[p + i] = 1

    def genHashTbl(self):
        substr = ""
        ti = 0
        # for x in range(0, len(self.inputText)):
        counter = 0
        while counter <= len(self.inputText):
            if counter < len(self.inputText):
                if not self.tmask[counter] and len(
                        substr) < self.s:  # if not masked
                    if not len(substr):
                        ti = counter
                    # add self.inputText letter to substr
                    substr += self.inputText[counter]
                elif len(substr) == self.s or self.tmask[counter] and len(
                        substr) == self.s:
                    counter -= 1
                    # add to the hashtable
                    if self.hashtable.get(substr) is None:
                        self.hashtable[substr] = [ti]
                    else:
                        self.hashtable[substr].append(ti)
                    substr = ""

            elif counter == len(self.inputText) and len(substr) == self.s:
                if self.hashtable.get(substr) is None:
                    self.hashtable[substr] = [ti]
                else:
                    self.hashtable[substr].append(ti)
            else:
                substr = ""
            counter += 1
        return self.hashtable  # remove this when done testing

    def matchPattern(self):
        psubstr = ""
        si = 0
        for x in range(0, len(self.pattern)):
            if not self.pmask[x] and len(psubstr) < self.s + 1:
                if not len(psubstr):
                    si = x
                # addself.inputText letter to substr
                psubstr += self.pattern[x]

            elif self.pmask[x] and len(psubstr) <= self.s:
                psubstr = ""

            if len(psubstr
                   ) == self.s or self.pmask[x] and len(psubstr) == self.s:

                start = self.hashtable.get(psubstr)
                if start is not None:
                    for elem in start:
                        if self.pattern[si:(
                                si + self.s)] == self.inputText[elem:(elem +
                                                                      self.s)]:
                            # removed -1 from s

                            k = self.s
                            while si + k < len(
                                    self.pattern) and elem + k < len(
                                        self.inputText) and self.pattern[
                                            si + k] == self.inputText[
                                                elem + k] and not self.pmask[
                                                    si + k] and not self.tmask[
                                                        elem + k]:
                                k += 1
                                # TODO FIX THE RESTART OF SCANNER WITH NEW S
                                #            if k > 2 * self.s:
                                #               self.s = k
                                # restart scanner withself.s== k
                                #              self.genHashTbl()
                                #          else:
                                if self.mml.get(k):
                                    self.mml[k].append((si, elem, k))
                                    self.maskArray(si, elem, k)

                                else:
                                    self.mml[k] = deque([(si, elem, k)])
                                    self.maskArray(si, elem, k)
                                # rec pattrn start, text start, and length of
                                # match
                                psubstr = ""
