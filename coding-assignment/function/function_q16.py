#write a function to calculate the power of a number without using **.


def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result
