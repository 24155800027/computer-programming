#Remove duplicate characters from a string.

def remove_duplicates(s):
    return ''.join(dict.fromkeys(s))
