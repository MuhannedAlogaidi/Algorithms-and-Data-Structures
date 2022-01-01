# ************************ Intersection of Two Sorted Arrays Uplevel *********************************
# DAM 11/15/2021
# Takes two SORTED! arrays and returns a list of intersection
# If the arrays aren't sorted, this code fails...
# Uses two pointers

def FindIntersection(array1, array2):
    # init vars
    index1 = 0
    index2 = 0
    result = []

    print(array1)
    print(array2)

    # loop while both pointers are within bounds
    while(index1 < len(array1) and index2 < len(array2)):
        print(array1[index1], array2[index2])

        # either 1st number is LESS THAN...
        if array1[index1] < array2[index2]:
            index1 += 1
        
        # or 1st number is GREATER THAN...
        elif array1[index1] > array2[index2]:
            index2 += 1

        # or 1st number is EQUAL TO the 2nd number
        else:
            # empty result?
            if len(result) == 0:
                # add 1st number
                result.append(array1[index1])

            else:
                # add number only if it's not a dupe of the previously added number
                if result.pop != array1[index1]:
                    result.append(array1[index1])

            index1 += 1
            index2 += 1

    return result

# Two SORTED! arrays with duplicates in both
FirstArray = [2, 3, 3, 4, 6, 8, 9, 11, 12, 15, 17]

SecondArray = [3, 5, 7, 8, 10, 11, 11, 13]

print(FindIntersection(FirstArray, SecondArray))
