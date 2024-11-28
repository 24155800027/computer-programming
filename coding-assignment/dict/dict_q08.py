#Find the intersection of two lists using a dictionary.
def intersection(lst1, lst2):
    dict1 = {item: True for item in lst1}
    return [item for item in lst2 if item in dict1]
