#Remove all occurrences of a specific element from a list.

def remove_all(lst, target):
    return [x for x in lst if x != target]
