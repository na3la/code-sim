import testtokenizer
from collections import Counter

tokenize = testtokenizer.tokenizer('../javahw1/fixed/')
tokenize.folderRead()

tokensumdict = tokenize.summaryDict.keys()

tokensumdict = list(tokensumdict)
vec = j.summaryDict[c[4]][0]
rvec = j.summaryDict[c[4]][1]
vec1 = j.summaryDict[c[3]][0]
rvec1 = j.summaryDict[c[3]][1]
vec = vec.split()
vec1 = vec1.split()
rvec = rvec.split()
rvec1 = rvec1.split()
k = Counter()
z = Counter()


for x, y in enumerate(vec):
    if k.get(y):
        k[y][0].append(x)
        k[y][1] += 1
        continue
    k[y] = [[x], 1]

for x, y in enumerate(vec1):
    if z.get(y):
        z[y][0].append(x)
        z[y][1] += 1
        continue
    z[y] = [[x], 1]
    
matchd = dict()
for key, v in k.items():
    if z.get(key):
        zset = set(z.get(key)[0])
        kset = set(v[0])
        i = zset.intersection(kset)
    if i is not None:
        for ke in i:
            matchd[ke] = key
            
class codematch():
    def __init__(self, token_vec_1, token_vec_2, raw_vec_1, raw_vec_2):
        self._token_vec_1 = token_vec_1.split()
        self._token_vec_2 = token_vec_2.split()
        self._raw_vec_1 = raw_vec_1.split()
        self._raw_vec_2 = raw_vec_2.split()
        self._t_vec_1_counter = Counter()
        self._t_vec_2_counter = Counter()
        self.match_dict = dict()
    
    def _gen_counters(self):
        
        
        for key, value in enumerate(self._token_vec_1):
            if self._t_vec_1_counter.get(value):
                self._t_vec_1_counter.[value][0].append(key)
                self._t_vec_1_counter.[value][1] += 1
                continue
            self._t_vec_1_counter[value] = [[key], 1]
        
        for key, value in enumerate(self._token_vec_2):
            if self._t_vec_2_counter.get(value):
                self._t_vec_2_counter.[value][0].append(key)
                self._t_vec_2_counter.[value][1] += 1
                continue
            self._t_vec_2_counter[value] = [[key], 1]
        
    def _gen_match_dict(self):
        
        for key, value in self._t_vec_1_counter.items():
            if self._t_vec_2_counter.get(key):
                _t_vec_1_set = set(self._t_vec_1_counter.get(key)[0])
                _t_vec_2_set = set(value[0])
                _intersect = _t_vec_1_set.intersection(_t_vec_2_set)
            if _intersect is not None:
                for index in _intersect:
                    self.match_dict[index] = key
                