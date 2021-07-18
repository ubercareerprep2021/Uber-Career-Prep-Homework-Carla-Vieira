"""
Sorting Exercise 4: Group Anagrams
Write a method to sort an array of strings so that all the anagrams are next to each other. Assume the average length of
the word as “k”, and “n” is the size of the array, where n >> k (i.e. “n” is very large in comparison to “k”). Do it in
a time complexity better than O[n.log(n)]
"""
from collections import defaultdict, Counter

def group_anagrams(words):
    list_words = []
    words_dict = defaultdict(list)

    for word in words:                        # it will take O(n)
        word_counter = Counter(word)          # it will take O(k). As it is inside the loop, O(n*k)
        words_dict[str(sorted(word_counter.items()))].append(word)

    for words in words_dict.values():         # it will take O(n)
        list_words.extend(words)

    return list_words

# Time Complexity
# O(n*k + n) ~= O(n*k)
# Space Complexity
# O(n*k)


