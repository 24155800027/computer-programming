#Reverse the order of words in a string.

def reverse_words(s):
    return ' '.join(s.split()[::-1])
