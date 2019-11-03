from gst.program_loop import prog_loop

""" Caller module for karp-rabin tilling. Creates mask arrays as well as match
dictionary."""


def take_text_pattern(text, pattern, min_match_len):

    """
        Args:
            text -> the text data to be used
            pattern -> the pattern data to be used
            min_match_len -> the minimum length of matching elements to be
                             considered a match.
        returns:
                prog_loop -> the main body of karp-rabin tilling
    """

    t_mask = [False] * len(text)
    p_mask = [False] * len(pattern)
    match_list_dict = dict()

    return prog_loop(text, pattern, min_match_len, t_mask, p_mask,
                     match_list_dict)
