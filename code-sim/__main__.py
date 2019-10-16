from itertools import combinations_with_replacement

import pandas as pd
from sklearn import preprocessing

import lib.distance_metrics as dm
from gst.new_kr import take_text_pattern
from lib._diff_lib_util import return_ratio
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

    diff_ratio_check = pd.DataFrame(columns=["ID", "Diff", "ltt_ldd", "avg_ltt"])

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

        # small diff (identical == 1) small ltt_ldd (identical == 0)
        if not dat[x][y]:
            continue
#        if dat[x][y] < .3:
#            diff_ratio_check["ID"].append([x, y])
#            diff_ratio_check["Diff"].append(dat_diff[x][y])
#            diff_ratio_check["ltt_ldd"].append(dat[x][y])
#            diff_ratio_check["avg_ltt"].append(dat2[x][y])
        #if dat_diff[x][y] - dat[x][y] < .5:
        #    diff_ratio_check.append(
        #        (pair, dat_diff[x][y], dat[x][y], dat2[x][y]))

    # scale dm.avg_ltt w/ min-max
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1), copy=False)

    min_max_scaler.fit_transform(dat2)

    dat.to_csv('ltt_ldd.csv', sep=',')
    dat2.to_csv('avg_ltt.csv', sep=',')
    dat_diff.to_csv('diff.csv', sep=',')

    f = open('diff_ratio.txt', 'w')
    f.write(diff_ratio_check.__str__())


main()
