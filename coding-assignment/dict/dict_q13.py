#You are given two lists. One represents the keys and the other represents the values. Create a dictionary using these lists.
def create_dict(keys, values):
    return dict(zip(keys, values))
