import hacking as hk
import testtokenizer as tk


def __main__():

    src_folder = "../javahw1/fixed"  # input(">> source file folder? ")

    token = tk.tokenizer(src_folder)
    token.folderRead()
    user_id_list = sorted(token.summaryDict.keys())  # need to be sorted?
    TEMP_MATCH_ARR = []
    metric = 0

    for index, uid in enumerate(user_id_list):

        token_vec_1 = token.summaryDict[uid][0]
        raw_vec_1 = token.summaryDict[uid][1]

        for uid2 in user_id_list:

            token_vec_2 = token.summaryDict[uid2][0]
            raw_vec_2 = token.summaryDict[uid2][1]

            match, t = hk.codematch(token_vec_1, token_vec_2,
                                    raw_vec_1, raw_vec_2).match()
            TEMP_MATCH_ARR.append((uid, uid2, match))
            metric += t

    print(metric/pow(len(user_id_list), 2))
    return TEMP_MATCH_ARR