#You are given two dictionaries. Merge them into a single dictionary, combining the values of any matching keys.
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # Copy first dictionary
    merged.update(dict2)  # Update with second dictionary
    return merged
