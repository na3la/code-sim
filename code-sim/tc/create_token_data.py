from tc.TokenObject import TokenObject
from tc.open_lex import _open_lex
from tc.file_feeder import _file_feeder
from tc.folder_location import _option

# TODO change type comparison to isinstance
# TODO add return statement for consistency
"""
This function calls _open_lex(...) which generates a tokenized version of
each source code file, as well as a non-tokenized string version.

It checks if each element is of type 'str', which indicates the element is a
string equivalent to the result of fstream.read(). These string objects are
appended to raw_list for use in diff comparison. The other possible type is
TokenObject. These are appended to temp_list until 'EOF'
is detected, at which point temp_list is appended to obj_matrix and temp_list
is cleared.
"""


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
