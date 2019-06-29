import testtokenizer
from collections import Counter

# should match_dict be sorted by key/index?


class codematch():
    """
    Obj Parameters: Token string from src_file_1, token string from
    src_file_2, untokenized code string from src_file_1, untokenized code
    string from src_file_2.

    Split strings into string arrays. Declare Counters and Dict.
"""

    def __init__(self, token_vec_1, token_vec_2, raw_vec_1, raw_vec_2):
        self._token_vec_1 = token_vec_1.split()
        self._token_vec_2 = token_vec_2.split()
        self._raw_vec_1 = raw_vec_1.split()
        self._raw_vec_2 = raw_vec_2.split()
        self._t_vec_1_counter = Counter()
        self._t_vec_2_counter = Counter()
        self.match_dict = dict()

    def _gen_counters(self):

        """
        Populate Counters with token as token and 2D array holding indices of
        token location and count of token within string

        For loop parameters:
        index -> enumeration number. It is the index of the token within the
        token array.
        token -> token from token array.

        End Result:
        two Counters which have tokens made up of tokens and indexs which hold
        the location of that token within the the string and the number of
        times the token is seen within the string.
        """

        for index, token in enumerate(self._token_vec_1):
            if self._t_vec_1_counter.get(token):
                self._t_vec_1_counter[token][0].append(index)
                self._t_vec_1_counter[token][1] += 1
                continue
            self._t_vec_1_counter[token] = [[index], 1]

        for index, token in enumerate(self._token_vec_2):
            if self._t_vec_2_counter.get(token):
                self._t_vec_2_counter[token][0].append(index)
                self._t_vec_2_counter[token][1] += 1
                continue
            self._t_vec_2_counter[token] = [[index], 1]

    def _gen_match_dict(self):

        """
        Populate match_dict with common locations of tokens. Iterate through
        vec_1_counter and check for presence of token in vec_2_counter. If
        present, create set of indices array of token for arrrays in vec_1 and
        vec_2. Next, to get common indices, take intersection of these sets.
        If _intersect is not None, ie is not the empty set, iterate through
        _intersect and set each index as a token in match_dict with token as
        index.
        """

        for token, index in self._t_vec_1_counter.items():
            if self._t_vec_2_counter.get(token):
                _t_vec_1_set = set(self._t_vec_1_counter.get(token)[0])
                _t_vec_2_set = set(index[0])
                _intersect = _t_vec_1_set.intersection(_t_vec_2_set)
            if _intersect is not None:
                for index in _intersect:
                    self.match_dict[index] = token

    def match(self):

        self._gen_counters()
        self._gen_match_dict()

        return self.match_dict
