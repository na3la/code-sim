import os
# TODO remove hard coded path
import javac_parser
import re
from dataclasses import dataclass


def __str_format(file_read_str):
    return file_read_str.strip().replace('\n', ' ').replace('\t', ' ')


@dataclass(init=True, repr=True, eq=True)
class TokenObject:
    token: str
    value: str


def _open_lex(paths_to_file, uuid_list):
    java = javac_parser.Java()
    for path in paths_to_file:
        try:
            f = open(path, 'r')
            uuid_list.append(re.search(r'\d{6}', f.name)[0])
            yield from java.lex(__str_format(f.read()))
        finally:
            f.close()


def _file_feeder(path_to_folder):
    try:
        yield from (path_to_folder + file_name for file_name in
                    os.listdir(path_to_folder))
    except FileNotFoundError:
        print(f'FileNotFoundError: Check {path_to_folder} exists!')


def create_token_dict(uuid_list, obj_matrix):
    temp_list = []
    for x in _open_lex(
        _file_feeder(
                '/home/anon/notebooks/code-sim/tokenizer/javahw1/newfixed/'), uuid_list):

        if x[0].__eq__('EOF'):
            obj_matrix.append(temp_list.copy())
            temp_list.clear()
            continue
        temp_list.append(TokenObject(x[0], x[1]))
