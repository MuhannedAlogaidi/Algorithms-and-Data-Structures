# ************************ Recursion: Generate n combinations *********************************
# DAM 11/21/2021
# Given two integers n and k, return all possible combinations of k numbers out of 1 ...n
# will employ binary inclusion/exclusion, add backtracking

def worker(n, i, k, slate, results):

    # backtracking case
    if len(slate) == k:
        results.append(slate[:])
        return

    # base case
    if i > n:
        return 

    # recursive cases
    # exclusion
    worker(n, i + 1, k, slate, results)

    # inclusion using sandwich pattern
    slate.append(i)
    worker(n, i + 1, k, slate, results)
    slate.pop()


def combinations(n, k):
    results = []
    slate = []

    worker(n, 1, k, slate, results)

    return results


print(combinations(4, 2))

