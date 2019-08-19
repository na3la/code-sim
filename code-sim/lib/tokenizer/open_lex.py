import javac_parser
import re
from __str_format import __str_format


def _open_lex(paths_to_file, uuid_list):
    java = javac_parser.Java()
    for path in paths_to_file:
        try:
            f = open(path, 'r')
            uuid_list.append(re.search(r'\d{6}', f.name)[0])
            yield from java.lex(__str_format(f.read()))
        finally:
            f.close()
