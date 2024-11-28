#Sort a list of elements based on their frequency using a dictionary.
from collections import Counter
def sort_by_frequency(lst):
    freq = Counter(lst)
    return sorted(lst, key=lambda x: freq[x], reverse=True)
