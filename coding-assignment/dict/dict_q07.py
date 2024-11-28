#Given a list of strings, group anagrams together using a dictionary.
from collections import defaultdict
def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
