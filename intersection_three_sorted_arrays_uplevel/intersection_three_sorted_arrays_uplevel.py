# ************************ Intersection of Three Sorted Arrays Uplevel *********************************
# DAM 11/15/2021
# Takes three SORTED! arrays and returns a list of intersection
# If the arrays aren't sorted, this code fails...
# Uses two pointers

def FindIntersection(array1, array2, array3):
    index1 = 0
    index2 = 0
    index3 = 0
    result = []

    print(array1)
    print(array2)

    while(index1 < len(array1) and index2 < len(array2) and index3 < len(array3)):
        print(array1[index1], array2[index2], array3[index3])

        if array1[index1] < array2[index2]:
            index1 += 1

        elif array1[index1] > array2[index2]:
            index2 += 1

        elif array1[index1] < array3[index3]:
            index1 += 1

        elif array1[index1] > array3[index3]:
            index3 += 1

        else:
            if result.pop != array1[index1]:
                result.append(array1[index1])
                index1 += 1
                index2 += 1

    if len(result) == 0: result.append(-1)
                
    return result

# SORTED! arrays
FirstArray = [2, 5, 10]

SecondArray = [2, 3, 4, 10]

ThirdArray = [2, 4, 10]

print(FindIntersection(FirstArray, SecondArray, ThirdArray))

