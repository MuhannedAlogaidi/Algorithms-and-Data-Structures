# ************************ Recursion: Generate n combinations Adding up to Integer *********************************
# DAM 11/28/2021
# Given an integer array, generate all the unique combinations of the array numbers
# that sum up to a given target value
def worker(target, index, array_length, array, slate, results):
    # backtracking case

    if sum(slate, 0) == target:
        if slate[:] not in results:
            results.append(slate[:])
        return

    # base case
    if index == array_length:
        return

    # recursive cases
    # exclusion
    worker(target, index + 1, array_length, array, slate, results)

# inclusion using sandwich pattern

    slate.append(array[index])

    worker(target, index + 1, array_length, array, slate, results)

    slate.pop()

def combinations(array, n):
    results = []
    slate = []
    worker(n, 0, len(array), array, slate, results)
    return results

print(combinations([1, 3, 5], 9))

