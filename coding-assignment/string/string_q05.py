#Determine if two strings are anagrams of each other.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
