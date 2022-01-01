# ************************ Group The Numbers Uplevel *********************************
# DAM 11/19/2021
# Takes an array and returns a list partitioned into odd and even
# Even on left, odd on right
# Uses two pointers

def GroupNumbers(array):

    even_pointer = -1

    for i in range(0, len(array)):

        print(array)

        # if odd
        if (array[i] % 2 != 0):
            i += 1

        # swap & advance
        else:
            if even_pointer == -1: even_pointer += 1
            array[even_pointer], array[i] = array[i], array[even_pointer]
            even_pointer += 1

        print(array)

array = [6, 15, 2, 9, 11, 4, 8]

print(GroupNumbers(array))

# 6, 2, 4, 8, 11, 15, 9