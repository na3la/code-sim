""" distance metrics for use with __main__ """


def ltt_ldd(tiled_tokens_length, text_length, pattern_length):

    return abs(((tiled_tokens_length * 2) / (pattern_length + text_length)) -
               1)


def avg_ltt(tiled_tokens_length, text_length, pattern_length):

    if not tiled_tokens_length:
        return 0

    return ((((pattern_length + text_length) / 2) / tiled_tokens_length) - 1)
