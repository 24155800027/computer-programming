#Given a list of integers from 1 to n with one number missing, find the missing number.

def find_missing_number(lst, n):
    return sum(range(1, n + 1)) - sum(lst)

