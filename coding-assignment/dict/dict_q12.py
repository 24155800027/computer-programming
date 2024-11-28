#Write a program to find the intersection of two dictionaries, i.e., common keys with the same values.
def dict_intersection(dict1, dict2):
    return {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
