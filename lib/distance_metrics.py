""" distance metrics for use with __main__ """


def ltt_ldd(tiled_tokens_length, text_length, pattern_length):
    """
        length of tiled tokens * 2 / sum of pattern and text lengths

    """

    return abs(((tiled_tokens_length * 2) / (pattern_length + text_length)) -
               1)


def avg_ltt(tiled_tokens_length, text_length, pattern_length):
    """
        The average of pattern and text length / length of tokens tiled
    """

    if not tiled_tokens_length:
        return 0

    return ((((pattern_length + text_length) / 2) / tiled_tokens_length) - 1)
