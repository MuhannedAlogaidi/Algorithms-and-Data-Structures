# ************************ Recursion: Generate All Permutations Uplevel *********************************
# DAM 11/22/2021
# Given an array of unique numbers, return in any order all its permutations
# Uses MUTABLE data structures

def permutations(array):

    temp = []
    result = []

    worker(array, 0, [], result)
    return result

def worker(string, i, slate, result):
    
    # base case
    if i == len(string):
        if slate[:] not in result:
            result.append(slate[:])
        return

    # recursive case
    else:
        for pick in range(i, len(string)):
            string[i], string[pick] = string[pick], string[i]
            slate.append(string[i])

            worker(string, i + 1, slate, result)

            slate.pop()
            string[i], string[pick] = string[pick], string[i]

print(permutations([1, 2, 2]))


