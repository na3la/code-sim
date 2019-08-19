# read config file


def _readutil():
    try:
        f = open('.csconfig', 'r')
    except OSError:
        print('Unable to open .csconfig')

    path = f.read().strip()
    f.close()
    return path
