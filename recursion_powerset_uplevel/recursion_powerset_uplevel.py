# ************************ Recursion: Generate All Subsets (Powerset) Uplevel *********************************
# DAM 11/21/2021
# Generates all possible subsets of a given set;
# will employ binary inclusion/exclusion

def worker(string, i, slate, results):
    # base case
    if i == len(string):
        results.append(slate[:])
        return 

    # recursive cases
    # exclusion
    worker(string, i + 1, slate, results)

    # inclusion using sandwich pattern
    slate.append(string[i])
    worker(string, i + 1, slate, results)
    slate.pop()

    #return results

def subsets(string):
    results = []
    slate = []

    worker(string, 0, slate, results)

    print(results)

    return results

string = "xy"
print(subsets(string))
