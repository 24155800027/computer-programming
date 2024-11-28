#Write a program to remove specific keys from a dictionary.
def remove_keys(d, keys):
    for key in keys:
        if key in d:
            del d[key]
    return d
