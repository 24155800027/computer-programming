#Write a Python program to count the occurrences of each word in a string using a dictionary.
def word_count(string):
    words = string.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict
