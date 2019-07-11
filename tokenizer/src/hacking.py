import testtokenizer
import time
from collections import Counter

# should match_dict be sorted by key/index?
# TODO CONVERT CHECK_HASH TO CREATE HASHING DS IN HERE OR OTHER FILE
# also figure out dendrogram starting at zero and building up --> why the
# distance of 1 worked as no match


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

    def _check_hash(self):
        if hash(''.join(self._token_vec_1)) == hash(''.join(
                self._token_vec_2)) or not len(self._token_vec_1) or not len(
                    self._token_vec_2):
            f = open('DUPLICATES.txt', 'a')
            f.write("\n\n RAW STRINGS \n\n")
            f.write(' '.join(self._raw_vec_1) + '\n')
            f.write(' '.join(self._raw_vec_2) + '\n')
            f.write(' '.join(self._token_vec_1) + '\n')
            f.write(' '.join(self._token_vec_2) + '\n\n')
            f.close()
            return 0
        return 1

    def _gen_counters(self, counter, token_vec):

        for index, token in enumerate(token_vec):
            if counter.get(token):
                counter[token][0].append(index)
                counter[token][1] += 1
                continue
            counter[token] = [[index], 1]
        return counter

    def _gen_counters_helper(self):
        """
        Populate Counters with token as key and 2D array holding indices of
        token location and count of token within string as value.

        For loop parameters:
        index -> enumeration number. It is the index of the token within the
        token array.
        token -> token from token array.

        End Result:
        two Counters which have keys made up of tokens and values which hold
        the location of that token within the the string and the number of
        times the token is seen within the string.
        """
        self._gen_counters(self._t_vec_1_counter, self._token_vec_1)
        self._gen_counters(self._t_vec_2_counter, self._token_vec_2)

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
                _t_vec_1_set = set(index[0])
                _t_vec_2_set = set(self._t_vec_2_counter.get(token)[0])

                _intersect = _t_vec_1_set.intersection(_t_vec_2_set)
            else:
                continue
            if _intersect is not None:
                for index in _intersect:
                    self.match_dict[index] = token

    def match(self):

        if not self._check_hash():
            return (0)
        self._gen_counters_helper()
        self._gen_match_dict()

        print('ABOVE WITH')
        with open('txt.txt', 'a') as f:
            print('UNDER WITH')
            f.write("\n RAW STRINGS \n")
            f.write(' '.join(self._raw_vec_1) + '\n')
            f.write(' '.join(self._raw_vec_2) + '\n')
            f.write(' '.join(self._token_vec_1) + '\n')
            f.write(' '.join(self._token_vec_2) + '\n')
            f.write("\n MATCHING \n")
            if self.match_dict.keys():
                for indx in range(max(self.match_dict.keys())):
                    if self.match_dict.get(indx):
                        f.write(self._raw_vec_1[indx] + ' ')
                    else:
                        f.write("X ")

        return self.match_dict
