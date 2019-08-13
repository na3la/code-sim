import subprocess
import os
import os.path
from itertools import combinations_with_replacement


def _diff(src_a, src_b):
    return subprocess.Popen(
        ["diff", src_a, src_b],
        stdout=subprocess.PIPE,
    )


def _cat(diff):
    return subprocess.run(
        ["cat", "-A"],
        stdin=diff.stdout,
        stdout=subprocess.PIPE,
    )


def _gen_diff(uuid_a, uuid_b, fpath_a, fpath_b):

    if not os.path.isdir("diffs"):
        os.mkdir("diffs")
    if not os.path.isfile("diffs/" + str(uuid_a) + "_" + str(uuid_b) +
                          "_diff.txt") and not os.path.isfile("diffs/" + str(
                              uuid_b) + "_" + str(uuid_a) + "_diff.txt"):
        f = open("diffs/" + str(uuid_a) + "_" + str(uuid_b) + "_diff.txt", 'w')
        f.write(_cat(_diff(fpath_a, fpath_b)).stdout.decode())
        f.close()


def _gen_comb(dir_list):
    return combinations_with_replacement(dir_list, 2)


def gen_diff(
        folder_path="/home/anon/notebooks/code-sim/tokenizer/javahw1/newfixed/"
):

    for pair in _gen_comb(os.listdir(folder_path)):
        _gen_diff(pair[0][1:7], pair[1][1:7], folder_path + pair[0],
                  folder_path + pair[1])


gen_diff()
# TODO create CSV in same layout as others with values == # \n in _cat.stdout
# TODO test pycparser
