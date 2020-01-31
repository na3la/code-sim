from tc.create_token_data import _create_token_data

"""
This is the caller function for tokenization. It returns two dictionaries:

The first is a mapping of 'UUID'-->int to tokenized list. The tokenized list is
a 2d list of lists, where each inner list is made up of TokenObject.

The second dictionary is a mapping of 'UUID'-->int to raw list. The raw list is
a 1d list where each element is the raw file as read from fstream.read().
"""


def dict_builder():
    uuid_list, obj_matrix, raw_list = [], [], []
    _create_token_data(uuid_list, obj_matrix, raw_list)
    return dict(zip(uuid_list, obj_matrix)), dict(zip(uuid_list, raw_list))
