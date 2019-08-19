# helper function for path to read from


def _readutil():
    try:
        f = open('.csconfig', 'r')
    except OSError:
        print('Unable to open .csconfig')

    path = f.read().strip()
    f.close()
    return path


def _option():

    select = input(
        "Folder containing sources?(defaults to path in .csconfig) ")

    if select:
        return select

    return _readutil()
