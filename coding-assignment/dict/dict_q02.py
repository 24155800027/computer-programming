#Write a Python program to find the element that occurs most frequently in a list using a dictionary.
def most_frequent(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return max(freq, key=freq.get)
