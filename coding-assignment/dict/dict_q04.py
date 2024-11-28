#Given two lists, determine if the second list is a subset of the first one using dictionaries.
def is_subset(list1, list2):
    dict1 = {}
    for item in list1:
        dict1[item] = 1
    for item in list2:
        if item not in dict1:
            return False
    return True
