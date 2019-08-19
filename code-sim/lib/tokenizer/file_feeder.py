# a generator to create & yield a path to a file


import os


def _file_feeder(path_to_folder):
    try:
        yield from (path_to_folder + file_name for file_name in
                    os.listdir(path_to_folder))
    except FileNotFoundError:
        print(f'FileNotFoundError: Check {path_to_folder} exists!')
