import os
import os.path
"""
This function is a generator which generates file paths for each source code
file in path_to_folder.
"""


def _file_feeder(path_to_folder):
    try:
        yield from (os.path.join(path_to_folder, file_name)
                    for file_name in os.listdir(path_to_folder)
                    if file_name[-2:] == ".c")
    except FileNotFoundError:
        print(f'FileNotFoundError: Check {path_to_folder} exists!')
        exit()
