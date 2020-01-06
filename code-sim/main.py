from itertools import combinations_with_replacement

import pandas as pd
from sklearn import preprocessing

import lib.distance_metrics as dm
from gst.new_kr import take_text_pattern
from tc.dict_builder import dict_builder


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

    # scale dm.avg_ltt w/ min-max
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1),
                                                copy=False)

    min_max_scaler.fit_transform(dat2)

    dat.to_csv('ltt_ldd.csv', sep=',')
    dat2.to_csv('avg_ltt.csv', sep=',')
    dat_diff.to_csv('diff.csv', sep=',')

<<<<<<< HEAD:code-sim/main.py

=======
    f = open('diff_ratio.txt', 'w')
    f.write(diff_ratio_check.__str__())
    f.close()
    
>>>>>>> c3ea865d9df046ed0a7cd04e5ee898a598445368:code-sim/__main__.py
main()
