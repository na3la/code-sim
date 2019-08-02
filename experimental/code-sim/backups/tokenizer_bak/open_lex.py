import javac_parser


def _open_lex(paths_to_file):
    java = javac_parser.Java()
    for path in paths_to_file:
        try:
            f = open(path, 'r')
            yield from map(java.lex, f.readlines())
        finally:
            f.close()
