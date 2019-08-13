import os
import re
from dataclasses import dataclass

from cpp import caller


@dataclass(init=True, repr=True, eq=True)
class TokenObject:
    token: str
    value: str


def __str_format(file_read_str):
    return file_read_str.strip().replace('\n', ' ').replace('\t', ' ')


def _open_lex(paths_to_file, uuid_list):
    for path in paths_to_file:
        try:
            f = open(path, 'r')
            name, txt = f.name, f.read()
            f.close()
            yield txt
            uuid_list.append(re.search(r'\d{6}', name)[0])
            yield from caller(__str_format(txt), name)
        except FileNotFoundError:
            print("could not find {}", path)


def _file_feeder(path_to_folder):
    try:
        yield from (path_to_folder + file_name for file_name in
                    os.listdir(path_to_folder))
    except FileNotFoundError:
        print(f'FileNotFoundError: Check {path_to_folder} exists!')


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


def _create_token_data(uuid_list, obj_matrix, raw_list):
    temp_list = []
    for x in _open_lex(_file_feeder(_option()), uuid_list):

        if type(x) is str:
            raw_list.append(x)
            continue

        elif x[0].__eq__('EOF'):
            obj_matrix.append(temp_list.copy())
            temp_list.clear()
            continue
        temp_list.append(TokenObject(x[0], x[1]))


def dict_builder():
    uuid_list, obj_matrix, raw_list = [], [], []
    _create_token_data(uuid_list, obj_matrix, raw_list)
    # raw_list = diff_build()
    return dict(zip(uuid_list, obj_matrix)), dict(zip(uuid_list, raw_list))


def diff_build():
    raw_list = []
    for x in os.listdir('/home/anon/notebooks/datasets/os_c_hw/hw11/code_dir/'):
        f = open('/home/anon/notebooks/datasets/os_c_hw/hw11/code_dir/'+ x, 'r')
        raw_list.append(f.read())
        f.close()
    return raw_list

