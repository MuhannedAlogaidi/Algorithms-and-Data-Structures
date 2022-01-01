
# ************************ Two Sum Advanced Uplevel *********************************
# DAM 11/15/2021
# "Transform and conquer": advanced two sum solution based on pseudo code from Uplevel
# Takes raw array and transforms into hashtable, returning a list of tuples with all sum pairs

def two_sum(input, target):

    # init vars
    hashtable = {}      # dictionary for hashtable
    list = []           # list, in case we need to return the pair
    contains = False    # return value

    # loop through input array
    for n1 in input:

        # calculate second number based on input
        n2 = target - n1

        # 2nd number in hash table?
        if n2 in hashtable:
            # add tuple pair to list
            pair = (n1, n2)
            list.append(pair)

        else:
            # add to hashtable
            hashtable[n1] = 1

    return list


array = [8, 14, 10, 2, 8, 15, 1, 4, 11, 12, 6]

print(two_sum(array, 16))

