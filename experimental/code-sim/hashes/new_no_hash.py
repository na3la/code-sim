def mask_array(a, mask_a, b, mask_b, max_match):

    for i in range(max_match):
        if not mask_a[a + i]:
            mask_a[a + i] = True
        if not mask_b[b + i]:
            mask_b[b + i] = True


def masked_check(a_adj_pos, b_adj_pos, mask_a, mask_b):
    return mask_a[a_adj_pos] | mask_b[b_adj_pos]


def equality_check(TO_a, TO_b):
    return TO_a.token == TO_b.token
    # return TO_a.__eq__(TO_b)


def pos_increment(position, length, mask):
    if position == (length - 1) or length == sum(mask):
        return -1
    for elem in range(1, length - position):
        if not mask[position + elem]:
            return position + elem
    return -1


def _builder(range_, t_list_a, t_list_b, mask_a, mask_b, a_pos, b_pos):
    # breakpoint()
    for elem in range_:
        if equality_check(t_list_a[a_pos + elem],
                          t_list_b[b_pos + elem]) and not masked_check(
                              a_pos + elem, b_pos + elem, mask_a, mask_b):
            yield 1
        else:
            return 0


def scan_pattern(t_list_a, t_list_b, equality_check):

    LEN_A = len(t_list_a)
    LEN_B = len(t_list_b)
    mask_a = [False] * LEN_A
    mask_b = [False] * LEN_B

    min_match_length = 1
    max_match_length = 0
    length_tokens_tiled = 0
    match_list = dict()
    a_pos = 0
    b_pos = 0

    while True:  # max_match_length != min_match_length:
        max_match_length = min_match_length

        j = sum(
            _builder(range(LEN_A - a_pos), t_list_a, t_list_b, mask_a,
                     mask_b, a_pos, b_pos))

        if j == max_match_length:
            if match_list.get(j) is not None:
                match_list[j].append((
                    a_pos,
                    b_pos,
                    j,
                ))
            else:
                match_list[j] = [(
                    a_pos,
                    b_pos,
                    j,
                )]
        elif j > max_match_length:
            match_list[j] = [(
                a_pos,
                b_pos,
                j,
            )]
            max_match_length = j

        if match_list.get(max_match_length):
            for tupe in match_list.get(max_match_length):
                if not sum(mask_a[tupe[0]:tupe[0] + tupe[2]]) + sum(
                        mask_b[tupe[1]:tupe[1] + tupe[2]]):
                    mask_array(tupe[0], mask_a, tupe[1], mask_b, tupe[2])
                    length_tokens_tiled += max_match_length

        # breakpoint()
        a_pos = pos_increment(a_pos, LEN_A, mask_a)
        b_pos = pos_increment(b_pos, LEN_B, mask_b)

        if a_pos == -1 or b_pos == -1:
            break

    return length_tokens_tiled


def caller(list_dict, list_tuple):

    return scan_pattern(
        list_dict.get(list_tuple[0]), list_dict.get(list_tuple[1]),
        equality_check) if len(list_dict.get(list_tuple[0])) <= len(
            list_dict.get(list_tuple[1])) else scan_pattern(
                list_dict.get(list_tuple[1]), list_dict.get(list_tuple[0]),
                equality_check)
