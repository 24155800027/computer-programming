#Given a dictionary, find the key with the maximum value.
def max_value_key(d):
    return max(d, key=d.get)
