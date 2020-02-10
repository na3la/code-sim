from tc.open_lex_update import _lex_code
from tc.file_feeder import _file_feeder
from tc.folder_location import _option


def dict_builder():
    uuid_list, obj_matrix = [], []
    _lex_code(_file_feeder(_option()), uuid_list, obj_matrix)
    return dict(zip(uuid_list, obj_matrix))
