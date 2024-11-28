#Create a dictionary where the keys are words and the values are their frequencies from a list of words
def frequency_dict(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

