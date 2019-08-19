from gst.equality_check import equality_check_using


def get_matches(p, t, p_mask, t_mask, pattern, text):

    j = 0
    while p + j < len(pattern) and t + j < len(text) and equality_check_using(
            pattern[p + j],
            text[t + j]) and p_mask[p + j] is False and t_mask[t + j] is False:

        j += 1

    return j
