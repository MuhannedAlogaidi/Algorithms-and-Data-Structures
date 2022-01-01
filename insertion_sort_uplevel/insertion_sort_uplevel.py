# ************************ Insertion Sort Uplevel *********************************
# DAM 11/11/2021
# "Decrease and conquer" insertion sort based on pseudo code from Uplevel

def print_list(num_list):
    print(num_list)

def insertion_sort(original_list):

    length = len(original_list)

    # outer loop: 0 to the length of the list
    for i in range(0, length - 1):

        print(original_list)

        # store the value we're trying to place in a temp variable
        temp = original_list[i]

        print(temp)

        # the value at the current index
        current = i - 1

        print(current)

        # 
        while current >= 0 and original_list[current] > temp:

            # push the value at the current index to the right
            original_list[current + 1] = original_list[current]

            # decrement 
            current = current - 1

            original_list[current + 1] = temp

            print(original_list)

    return original_list


a = [10, 5, 7, 2, 8, 3, 9, 6, 1, 4]

insertion_sort(a)