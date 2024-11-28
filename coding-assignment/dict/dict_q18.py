#Given a dictionary, find the key with the minimum value.
def min_value_key(d):
    return min(d, key=d.get)

