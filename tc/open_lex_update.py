import re
from pygments import lex, lexers


def _lex_code(paths_to_file, uuid_list, obj_matrix):
    lexer = lexers.CLexer()
    for path in paths_to_file:
        try:
            with open(path, 'r') as fp:
                uuid = fp.name
                code = fp.read()
                uuid_list.append(re.search(r'\d{6}', uuid)[0])
                obj_matrix.append([*lex(code, lexer)])
        except FileNotFoundError:
            print(f'could not find {path}')
            exit()
