
# ************************ Dutch National Flag Uplevel *********************************
# DAM 11/19/2021
# 3-way partitioning based on pseudo code from Uplevel

def dutch_national_flag(arr):
    # order of colors is R, G, B
    # so R & G vars start outside the bounds
    # on left side
    r = -1
    g = -1

    ubound = len(arr)

    #if len(arr) <= 3:
    #    ubound += 1

    for i in range(0, ubound):
        print(arr)
        if array[i] == "R":
            g += 1
            array[i], array[g] = array[g], array[i]

            r += 1
            array[g], array[r] = array[r], array[g]

        elif array[i] == "G":
            g += 1
            array[i], array[g] = array[g], array[i]

        print(arr)

array = ["G", "R"]
#array = [8, "G", "B", "G", "G", "R", "B", "R", "G"]

print(dutch_national_flag(array))
