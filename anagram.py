"""
In the script I intend to show the order of magnitude of an Anagram
program using different algorithms.  An Anagram is simply
when two strings comprise of the same character and len.
For example: 'Python' and 'Typhon', 'Pan' and 'Nap'
"""

# Checking Off
"""
The first method to writing an anagram validator is to
check that each of the characters in the first string is
present in the second string.
"""


def anagram_solution1(w1, w2):
    """Checks and compare the characters and length of two strings\
        to see if they are an anagram of each other"""

    char_list = list(w2.lower())  # Converts the characters of the second \
    # string and stores it in a list

    index1 = 0
    anagram_status = True

    while index1 < len(w1.lower()) and anagram_status:
        index2 = 0
        found = False
        while index2 < len(char_list) and not found:
            if w1[index1] == char_list[index2]:
                found = True
            else:
                index2 = index2 + 1

        if found:
            char_list[index2] = None
        else:
            anagram_status = False

        index1 = index1 + 1
    return anagram_status  # The order of magnitude of the program is O(n ^ 2)


# Sort and Compare
"""
Anagrams consists of the same characters and length. Another way to validate
an anagram is to begin sorting each string alphatically from a to z. If the
strings are anagrams we will end up with the same string. Using Python's sort
method on the lists by simply converting each string to a list at the start.

NOTE: In python the sort method has a order of magnitude of O(n^2) / O(n log n)
decresing the performance of the algorithm.
"""


def anagram_solution2(w1, w2):
    char_list1 = list(w1)
    char_list2 = list(w2)

    char_list1.sort()
    char_list2.sort()

    index = 0
    matches = True

    while index < len(w1) and matches:
        if char_list1[index] == char_list2[index]:
            index += 1
        else:
            matches = False

    return matches


# Count and Compare
"""
In this method I took advantage of the fact that any two anagrams
will consists of the same number of characters, meaning the words
'pan' and 'nap' both have the same numbers of A's.
In order to validate that two strings are anagrams, first count
the number of times each character occurs. Since there are 26
alphabets in the english language, we can use a list of 26 counters,
one for each possible character. Each time a character is used we
increment the counter for that position.
"""


def anagram_solution(w1, w2):
    counter1 = [0] * 26
    counter2 = [0] * 26

    for character in range(len(w1)):
        pos = ord(w1[character]) - ord('a')
        counter1[pos] += 1

    for character in range(len(w2)):
        pos = ord(w2[character]) - ord('a')
        counter2[pos] += 1

    alphabets = 0
    anagram_status = True
    while alphabets < 26 and anagram_status:
        if counter1[alphabets] == counter2[alphabets]:
            alphabets += 1
        else:
            anagram_status = False

    return anagram_status
# In the code above there are two iterations used, both
# based on the order of magnitude O(n). The 3rd iteration
# The while loop, comparing two lists takes 26 steps since
# there are 26 possible characters in the strings. Adding
# it up will give an order of T(n) = 2n + 26. That is O(n)
