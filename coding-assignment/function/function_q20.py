#Write a function to find the longest word in a sentence.


def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

