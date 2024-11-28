#Find all indices of a given element in a list.

def find_indices(lst, target):
    return [i for i, val in enumerate(lst) if val == target]
