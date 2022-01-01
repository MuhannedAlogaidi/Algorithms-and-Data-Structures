
# ************************ Recursion: Generate All Subsets (Powerset) for Strings including Case Uplevel *********************************
# DAM 11/27/2021
# Generates all possible subsets of a given set;
# will employ binary inclusion/exclusion and include case
import numbers

def worker(string, i, slate, results):
    # base case
    if i == len(string) and slate[:] not in results:
        results.append(slate[:])
        return 

    # recursive cases
    if i < len(string) and isinstance(string[i], numbers.Number) == False:

        # exclusion: integers
        #worker(string, i + 1, slate, results)

        # inclusion: alpha character using sandwich pattern
        slate += string[i].upper()
        worker(string, i + 1, slate, results)
        slate = slate[:-1]

        slate += string[i].lower()
        worker(string, i + 1, slate, results)
        slate = slate[:-1]


def subsets(string):
    results = []
    slate = ""

    worker(string, 0, slate, results)

    return results

string = "123"
print(subsets(string))

