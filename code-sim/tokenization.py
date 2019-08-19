import os
import re
from dataclasses import dataclass

import javac_parser


@dataclass(init=True, repr=True, eq=True)
class TokenObject:
    token: str
    value: str


def __str_format(file_read_str):
    return file_read_str.strip().replace('\n', ' ').replace('\t', ' ')


def _open_lex(paths_to_file, uuid_list):
    java = javac_parser.Java()
    for path in paths_to_file:
        try:
            f = open(path, 'r')
            f_string = f.read()
            yield f_string
            uuid_list.append(re.search(r'\d{6}', f.name)[0])
            yield from java.lex(__str_format(f_string))
            f.close()

        except FileNotFoundError:
            print(path + " not found")


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


def _create_token_data(uuid_list, obj_matrix, raw_string_list):
    temp_list = []
    for x in _open_lex(_file_feeder(_option()), uuid_list):
        if type(x) is str:
            raw_string_list.append(x)
            continue
        elif x[0].__eq__('EOF'):
            obj_matrix.append(temp_list.copy())
            temp_list.clear()
            continue
        temp_list.append(TokenObject(x[0], x[1]))


def dict_builder():
    uuid_list, obj_matrix, raw_string_list = [], [], []
    _create_token_data(uuid_list, obj_matrix, raw_string_list)
    return dict(zip(uuid_list, obj_matrix)), dict(zip(uuid_list, raw_string_list))
