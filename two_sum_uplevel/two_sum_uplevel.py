
# ************************ Two Sum Uplevel *********************************
# DAM 11/15/2021
# "Transform and conquer": simple boolean two sum solution based on pseudo code from Uplevel
# Take raw array and transform into hashtable

def two_sum(input, target):

    # init vars
    hashtable = {}      # dictionary for hashtable
    list = []           # list, in case we need to return the pair
    contains = False    # return value

    # loop
    for n1 in input:

        # calculate second number based on input
        n2 = target - n1

        # 2nd number in hash table?
        if n2 in hashtable:
            # set true
            contains = True
        else:
            # add to hashtable
            hashtable[n1] = 1

    return contains


array = [10, 2, 8, 15, 1, 4, 11]

print(two_sum(array, 16))
