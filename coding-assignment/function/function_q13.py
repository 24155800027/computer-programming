#Write a function to generate a list of even numbers up to a given number n.


def generate_evens(n):
    return [x for x in range(n + 1) if x % 2 == 0]
