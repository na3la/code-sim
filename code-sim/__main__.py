import pandas as pd
from tc.dict_builder import dict_builder
from gst.new_kr import take_text_pattern
from _diff_lib_util import return_ratio
from itertools import combinations_with_replacement
import distance_metrics as dm


def main():

    token_dict, raw_dict = dict_builder()
    fileuuids = combinations_with_replacement(token_dict.keys(), 2)

    dat = pd.DataFrame(index=sorted(token_dict.keys()),
                       columns=sorted(token_dict.keys()))
    dat2 = pd.DataFrame(index=sorted(token_dict.keys()),
                        columns=sorted(token_dict.keys()))
    dat_diff = pd.DataFrame(index=sorted(token_dict.keys()),
                            columns=sorted(token_dict.keys()))

    for pair in fileuuids:

        x, y = pair
        length_tiled_tokens = take_text_pattern(token_dict.get(x),
                                                token_dict.get(y), 1)

        dat[x][y] = dm.ltt_ldd(length_tiled_tokens, len(token_dict.get(x)),
                               len(token_dict.get(y)))
        dat[y][x] = dat[x][y]

        dat2[x][y] = dm.avg_ltt(length_tiled_tokens, len(token_dict.get(x)),
                                len(token_dict.get(y)))
        dat2[y][x] = dat2[x][y]

        dat_diff[x][y] = return_ratio(raw_dict.get(x), raw_dict.get(y))

        dat_diff[y][x] = dat_diff[x][y]

    breakpoint()


main()
