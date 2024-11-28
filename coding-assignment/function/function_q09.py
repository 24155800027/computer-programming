#Write a function to check if a number is an Armstrong number.


def is_armstrong(num):
    digits = list(map(int, str(num)))
    return num == sum(d ** len(digits) for d in digits)
