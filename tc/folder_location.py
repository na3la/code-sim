from tc.file_read_util import _read_util

"""
This function prompts the user for a folder path, which leads to source code
files.
"""


def _option():

    select = input(
        "Folder containing sources?(defaults to path in .csconfig) ")

    if select:
        return select

    return _read_util()
