# -*- coding: utf-8 -*-

"""

Greedy String Tiling


This code is closely based on the pseudocode in Section 2 of:

Michael J. Wise, String Similarity via Greedy String Tiling and Running Karp-Rabin Matching, 1993.


Created on Thu Jun  6 16:14:22 2019

@author: Glenn Bruns

"""


# return the similarity value for strings s1 and s2

def greedy_string_tiling(s1, s2, min_match_len = 1):

    P = list(s1)

    T = list(s2)

    

    len_tiled = 0

    P_mark = [False]*len(P)    # a boolean mask is used for marking

    T_mark = [False]*len(T)

    while True:
        # find all maximal matches

        match_list = []

        maxmatch = min_match_len

        for p in range(len(P)):

            for t in range(len(T)):

                j = 0

                while p+j < len(P) and t+j < len(T) and P[p+j].token == T[t+j].token and not P_mark[p+j] and not T_mark[t+j]:

                    j += 1

                if j == maxmatch:

                    match_list.append([p,t,j])

                elif j > maxmatch:

                    maxmatch = j

                    match_list = [[p,t,j]]

                    

        # maximal matches become tiles if not occluded by tiles laid earlier

        # note that the maximal matches can overlap (share tokens)

        for match in match_list:

            p,t,j = match

            if not any(P_mark[p:(p+j)]) and not any(T_mark[t:(t+j)]):

                # create new tile

                for j in range(maxmatch):

                    P_mark[p+j] = True

                    T_mark[t+j] = True

                len_tiled += maxmatch

                

        if maxmatch == min_match_len:

            break

    

    return len_tiled
