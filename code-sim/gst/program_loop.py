from gst.get_matches import get_matches

"""

This is an implementation of Section 2 of:

Michael J. Wise, String Similarity via Greedy String Tiling and

Running Karp-Rabin Matching, 1993.

"""


def prog_loop(text, pattern, min_match_len, t_mask, p_mask, match_list_dict):
    """

       It creates a mask for the pattern and text, then looks for equality at
       each index. if equality is found, index-incrementer "j" is incremented
       and equality is checked again. The match start's and length are added to
       a dictionary, and the match length is added to "len_tiled". The loop
       breaks if max_match == min_match_len.

        Args:
             text -> the text to be checked, must be a numerically indexable
                     iterable
             pattern -> the pattern to be checked, must be a numerically
                        indexable iterable
             min_match_len -> an integer indicating the minimum length of
                              matching elements to be considered a match
             t_mask -> text mask array
             p_mask -> pattern mask array
             match_list_dict -> dictionary containing match length, start, and
                                endindices
        returns:
                len_tiled -> an Int, total length of tokens tiled

    """
    len_tiled = 0
    while True:

        max_match = min_match_len

        for p in range(len(pattern)):

            for t in range(len(text)):

                j = get_matches(p, t, p_mask, t_mask, pattern, text)

                if j == max_match and j in match_list_dict:
                    match_list_dict[j].append((p, t, j,))

                elif j == max_match:
                    match_list_dict[j] = [(p, t, j,)]

                elif j > max_match:
                    match_list_dict[j] = [(p, t, j,)]
                    max_match = j

        if match_list_dict.get(max_match):
            for match in match_list_dict.get(max_match):
                P, T, J = match

                if not any(p_mask[P : P + J]) and not any(t_mask[T : T + J]):

                    for k in range(max_match):
                        p_mask[P + k] = True
                        t_mask[T + k] = True

                    len_tiled += max_match

        if max_match == min_match_len:
            break

    return len_tiled
