#Flatten a nested list into a single list.

def flatten_list(nested_lst):
    return [item for sublist in nested_lst for item in sublist]

