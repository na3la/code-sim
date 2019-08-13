class gst():
    def __init__(self, itext, pattern, minmatchlen):

        self.itext = itext
        self.pattern = pattern
        self.tmask = [0] * len(self.itext)
        self.pmask = [0] * len(self.pattern)
        self.length_of_tokens_tiled = 0
        self.minmatchlen = minmatchlen
        self.matchlist = dict()
        self.gen_prop = 0

    def maskArray(self, p, t, maxmatch):

        for i in range(maxmatch):
            if self.tmask[t + i] != 1:
                self.tmask[t + i] = 1

            if self.pmask[p + i] != 1:
                self.pmask[p + i] = 1

    def ret(self):
        print(self.matchlist)

    def equality_check(self, TO_a, TO_b):
        # test
        return TO_a == TO_b
        #return TO_a.token == TO_b.token
        #return TO_a.__eq__(TO_b)

    def scanPattern(self):

        maxmatch = 0

        while maxmatch != self.minmatchlen:
            # repeat
            maxmatch = self.minmatchlen

            # get first unmarked token of pattern
            for p in enumerate(self.pattern):
                if self.pmask[p[0]]:
                    continue
                for t in enumerate(self.itext):
                    if self.tmask[t[0]]:
                        continue
                    j = 0
                   # if (len(self.itext) == len(self.pattern) == maxmatch):
                   #     return 0
                    while len(self.pattern) > (p[0] + j) and len(
                            self.itext) > (t[0] + j) and self.equality_check(
                                self.pattern[p[0] + j],
                                self.itext[t[0] + j]) and not self.pmask[
                                    p[0] + j] and not self.tmask[t[0] + j]:
                        j += 1
                    if j == maxmatch:
                        if self.matchlist.get(j) is not None:
                            self.matchlist[j].append((p[0], t[0], j))
                        else:
                            self.matchlist[j] = [(p[0], t[0], j)]
                    elif j > maxmatch:
                        self.matchlist[j] = [(p[0], t[0], j)]
                        maxmatch = j

            if self.matchlist.get(maxmatch):
                for elem in self.matchlist.get(maxmatch):
                    if not sum(
                            self.pmask[elem[0]:elem[0] + elem[2]]) and not sum(
                                self.tmask[elem[1]:elem[1] + elem[2]]):
                        for index in range(maxmatch):
                            self.maskArray(elem[0], elem[1], elem[2])
                        self.length_of_tokens_tiled += maxmatch

    def gprop(self):
        for key in self.matchlist:
            self.gen_prop += key * len(self.matchlist[key])
