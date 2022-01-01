# ************************ Dynamic Programming: Football Score *********************************
# DAM 12/9/2021
# Given N distinct integers in a sorted array, build a balanced binary search tree.

def footballScore(final_score):
    if final_score < 0: return 0

    score_combos = [6]

    score_combos[0] = 1

    for i in xrange(len(score_combos)):
        if (i <= final_score):
