#You are given a list of integers. Write a Python program to count the frequency of each number using a dictionary.
#solution:

def count_frequency(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
