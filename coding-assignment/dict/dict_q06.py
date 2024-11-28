#Write a program to swap the keys and values of a dictionary.
def swap_keys_values(d):
    return {v: k for k, v in d.items()}
