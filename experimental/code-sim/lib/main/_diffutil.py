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
                          "_diff.txt") and os.path.isfile("diffs/" +
                                                          str(uuid_b) + "_" +
                                                          str(uuid_a) +
                                                          "_diff.txt"):
        f = open("diffs/" + str(uuid_a) + "_" + str(uuid_b) + "_diff.txt")
        f.write(_cat(_diff(fpath_a, fpath_b)).stdout.decode())
        f.close()

def gen_diff(folder_path):
   # TODO generate combinations_with_replacement of os.listdir(folderpath)
   # TODO feed filepaths and uuids to _gen_diff ((uuids --> filename[1:7]))
   # TODO create CSV in same layout as others with values == # lines in diffs
   # TODO test
   # TODO test pycparser




