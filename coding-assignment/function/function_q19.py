#Write a function to calculate the average of a list of numbers.


def average(lst):
    return sum(lst) / len(lst) if lst else 0
