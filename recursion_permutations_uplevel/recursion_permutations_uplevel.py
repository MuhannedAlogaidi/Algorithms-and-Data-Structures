# ************************ Recursion: Generate All Permutations Uplevel *********************************
# DAM 11/22/2021
# Given an array of unique numbers, return in any order all its permutations
# Uses immutable data structures

def permutations(array):

    temp = []
    result = []

    worker(temp, array, result)

    return result

def worker(slate, array, result):
    
    # base case
    if len(array) == 0:
        result.append(slate)

    # recursive case
    else:
        for i in range(len(array)):
            #slate.append(array[i])
            #array_temp = array[i + 1:]

            #print(slate+[array[i]])
            #print(array[:i] + array[i + 1:])
            worker(slate+[array[i]], array[:i]+array[i + 1:], result)

    return result


print(permutations([1, 2, 3]))

