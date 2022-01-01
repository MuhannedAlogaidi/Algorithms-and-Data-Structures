
# ************************ Recursion: n Queens Uplevel *********************************
# DAM 11/24/2021
# Given an integer n, find all the possible ways to position n queens
# on an n x n chessboard so that no two queens attack each other

# worker function to drive recursion
# n: integer to build n x n grid
# i: index (counter)
# slate: holds current state of partial solution
# results: global bag to hold final solution
def worker(n, i, slate, results):

    # backtracking case
    if is_Conflict(slate) == True:
        return

    # base case
    if i >= n:
        results.append(slate[:])
        return 

    # recursive cases
    for column in range(0, n):
        slate.append(column)
        worker(n, i + 1, slate, results)
        slate.pop()

# function to determine if there's a positional conflict
def is_Conflict(slate):
    if len(slate) <= 1:
        return False

    last = len(slate) - 1

    for q in range(0, last):

        #check for column violations
        if slate[q] == slate[last]:
            return True

        # check for diagonal violation: calculate slope 
        if abs(slate[q] - slate[last]) == abs(last - q):
            return True

    return False

def create_Qlist(input):
    qlist = []
    k = len(input)
    for i in range(0, k):
        qlist.append(create_Qstring(input[i], k))
    return qlist

def create_Qstring(n, k):
    qstring = ""
    temp = map(lambda x: 'q' if x == n else '-', range(0, k))
    tempList = list(temp)
    
    for k in tempList:
        qstring += k   
    return qstring

# function to return list of combos for queen positions
def n_queens(num):
    results = []
    slate = []
    queens = []

    worker(num, 0, slate, results)

    # translate list of integers to q-hyphen format
    for combo in results:
        queens.append(create_Qlist(combo))

    return queens

num = 5
print(n_queens(num))

