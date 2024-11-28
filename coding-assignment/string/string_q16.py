#Generate all permutations of a string.

from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]
