#Write a function to find all factors of a given number.


def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
