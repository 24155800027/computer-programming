#Write a program to count the number of unique words in a sentence using a dictionary.
def count_unique_words(sentence):
    words = sentence.split()
    word_dict = {}
    for word in words:
        word_dict[word] = 1
    return len(word_dict)
