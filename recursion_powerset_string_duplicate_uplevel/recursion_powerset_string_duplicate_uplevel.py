
# ************************ Recursion: Generate All Subsets (Powerset) for Strings with Duplicates Uplevel *********************************
# DAM 11/28/2021
# Given a string that might contain duplicate characters, 
# find all the possible distinct subsets of that string

def worker(string, i, slate, results):
    # base case
    if i == len(string):
        if slate not in results:
            results.append(slate[:])
            return
    else:
        # recursive cases
        # exclusion
        worker(string, i + 1, slate, results)

        # inclusion using sandwich pattern
        slate += string[i]
        worker(string, i + 1, slate, results)
        slate = slate[:-1]


def subsets(string):
    results = []
    slate = ""

    worker(string, 0, slate, results)

    return results

string = "dc"
print(subsets(string))

