#Write a function to find the second largest number in a list.

def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) > 1 else None
