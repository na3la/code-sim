from gst.program_loop import prog_loop


def take_text_pattern(text, pattern, min_match_len):
    t_mask = [False] * len(text)
    p_mask = [False] * len(pattern)
    match_list_dict = dict()

    return prog_loop(text, pattern, min_match_len, t_mask, p_mask,
                     match_list_dict)
