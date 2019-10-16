""" This uses difflib to calculate a ratio of matching elements. It uses the
absolute value of ratio - 1 so a 100% match is 0 and 0% is 1. This keeps in
line with format of distance metrics. """

import difflib


def return_ratio(f_string_a, f_string_b):
    return abs(
        difflib.SequenceMatcher(None, f_string_a, f_string_b).ratio() - 1)
