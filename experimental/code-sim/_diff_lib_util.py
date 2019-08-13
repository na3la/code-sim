import difflib


def return_ratio(f_string_a, f_string_b):
    return difflib.SequenceMatcher(None, f_string_a, f_string_b).ratio()
