from gst.equality_check import equality_check_using

""" This is a utility module for getting matches from text and pattern """


def get_matches(p, t, p_mask, t_mask, pattern, text):

    """ Args:
            p -> current pattern index
            t -> current text index
            p_mask -> pattern mask array
            t_mask -> text mask array
            pattern -> the pattern array
            text -> the text

        returns:
                j -> an integer representing match length

        This function takes p and t, which are the current positions in the
        pattern and text arrays. j is a slider which increments if the current
        elements match, and is returned when match ends. This (j) is how match
        length is tracked.
    """

    j = 0
    while p + j < len(pattern) and t + j < len(text) and equality_check_using(
            pattern[p + j],
            text[t + j]) and p_mask[p + j] is False and t_mask[t + j] is False:

        j += 1

    return j
