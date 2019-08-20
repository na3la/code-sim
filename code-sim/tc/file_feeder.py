import os

"""
This function is a generator which generates file paths for each source code
file in path_to_folder.
"""


def _file_feeder(path_to_folder):
    try:
        yield from (path_to_folder + file_name for file_name in
                    os.listdir(path_to_folder))
    except FileNotFoundError:
        print(f'FileNotFoundError: Check {path_to_folder} exists!')
