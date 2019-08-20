import re
from tc.format_comments import format_comments
from tc.str_format import _str_format
from cpp_test import caller

"""
This function generates source code files. It opens the file, formats the
inline comments, extracts the student uuid for the uuid_list, yields
fstream.read() string for raw_list, formats spacing within the fstream.read()
string before feeding to caller --> tokenizer
"""


def _open_lex(paths_to_file, uuid_list):
    for path in paths_to_file:
        try:
            f = open(path, 'r+')
            format_comments(f)
            f.seek(0)
            name, txt = f.name, f.read()
            f.close()
            yield txt
            uuid_list.append(re.search(r'\d{6}', name)[0])
            yield from caller(_str_format(txt), name)
        except FileNotFoundError:
            print("could not find {}", path)
            exit()
