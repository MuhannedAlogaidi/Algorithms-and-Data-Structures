
# ************************ Merge Sort Uplevel *********************************
# DAM 11/15/2021
# "Divide and conquer" insertion sort based on pseudo code from Uplevel
import math

def print_list(num_list):
    print(num_list)

def merge_sort(array):
    worker(array)

    return array

def worker(original_list):
    # base case
    if len(original_list) <= 1:
        return
    
    # compute mid point
    mid = len(original_list)//2
    # mid = math.floor(len(original_list)/2)
    print("Midpoint: ", mid)
    
    # divide into halves
    lefthalf = original_list[:mid]
    print("Left array: ", lefthalf)
    righthalf = original_list[mid:]
    print("Right array: ", righthalf)
    
    # recursive calls
    # numbers inserted into stack: LIFO
    merge_sort(lefthalf)
    print_list(lefthalf)
    
    merge_sort(righthalf)
    print_list(righthalf)
    
    # init counters for left, right, and original lists
    i = 0
    j = 0
    k = 0
    
    # reassemble the list
    # combine left and right index in sorted order
    # loop: ensure that the pointers i and j never 
    # exceed the length of either halves
    while i < len(lefthalf) and j < len(righthalf):
        # insert the smaller number into the original list
        if lefthalf[i] <= righthalf[j]:
            original_list[k] = lefthalf[i]
            
            i = i + 1
        else:
            original_list[k] = righthalf[j]
            j = j + 1
            
        k = k + 1
    
    # insert lefthalf leftovers into original list
    while i < len(lefthalf):
        original_list[k] = lefthalf[i]
        
        i = i + 1
        k = k + 1
        
    # insert righthalf leftovers into the original list
    while j < len(righthalf):
        original_list[k] = righthalf[j]
        
        j = j + 1
        k = k + 1

array = [21, 16, 10, 5, 7, 13, 2, 8, 19, 12, 14, 15, 3, 9, 18, 6, 1, 4, 11, 20, 17]

print(merge_sort(array))