#Find all elements in a list that appear more than n/k times.


from collections import Counter
def find_elements(lst, k):
    n = len(lst)
    freq = Counter(lst)
    return [key for key, count in freq.items() if count > n // k]

