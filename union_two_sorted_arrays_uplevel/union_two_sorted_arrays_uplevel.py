# ************************ Union of Two Sorted Arrays Uplevel *********************************
# DAM 11/16/2021
# Takes two SORTED! arrays and returns a list of union
# If the arrays aren't sorted, this code fails...
# Uses two pointers

def FindUnion(array1, array2):
    # init vars
    index1 = 0
    index2 = 0
    result = []

    print(array1)
    print(array2)

    # loop to drive processing
    while(index1 < len(array1) and index2 < len(array2)):
        print(array1[index1], array2[index2])

        if array1[index1] < array2[index2]:
            result.append(array1[index1])
            index1 += 1

        elif array1[index1] > array2[index2]:
            result.append(array2[index2])
            index2 += 1

        else:
            #if len(result) > 0 and result.pop != array1[index1]:
                result.append(array1[index1])
                index1 += 1
                index2 += 1

    while(index1 < len(array1)):
        result.append(array1[index1])
        index1 += 1

    while(index2 < len(array2)):
        result.append(array2[index2])
        index2 += 1

    return result

# SORTED! arrays
FirstArray = [2, 3, 4, 6, 8, 9, 11, 12, 15, 17]

SecondArray = [3, 5, 7, 8, 10, 11, 13]

print(FindUnion(FirstArray, SecondArray))

