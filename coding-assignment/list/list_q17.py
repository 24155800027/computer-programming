#Generate all possible subsets of a given list.

from itertools import combinations
def generate_subsets(lst):
    subsets = []
    for i in range(len(lst) + 1):
        subsets.extend(combinations(lst, i))
    return subsets
