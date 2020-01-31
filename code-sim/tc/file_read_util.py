"""
This function attempts to read a folder path from .csconfig.

.csconfig: used to store source code folder path, for repeated use.
"""

# TODO allow multiple folder paths to be stored and prompt user for selection
# of one
# TODO check for trailing '/' in folder path


def _read_util():
    try:
        f = open('.csconfig', 'r')
        path = f.read().strip()
        f.close()
        return path
    except OSError:
        print('Unable to open .csconfig')
        exit()

