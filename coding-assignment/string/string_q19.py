#Count the frequency of each word in a string.

from collections import Counter
def word_frequency(s):
    return Counter(s.split())
