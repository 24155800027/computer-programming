#Write a program that returns a dictionary containing the keys that are in the first dictionary but not in the second one.
def dict_difference(dict1, dict2):
    return {key: dict1[key] for key in dict1 if key not in dict2}

