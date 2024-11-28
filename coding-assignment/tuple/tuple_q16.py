#Merge two tuples, ensuring no duplicates.

def merge_unique(t1, t2):
    return tuple(set(t1) | set(t2))
