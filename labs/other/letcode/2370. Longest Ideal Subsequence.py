import string
from collections import defaultdict
def longestIdealString(s: str, k: int) -> int:
    # creates and populates a map of valid characters for each letter present in s
    letters_used = set(s)
    neighbours = {c: {c} for c in letters_used}
    for letter in neighbours:
        for i in range(1, k+1):
            upper_bound = chr(ord(letter) + i)
            lower_bound = chr(ord(letter) - i)
            if upper_bound in letters_used:
                neighbours[letter].add(upper_bound)
            if lower_bound in letters_used:
                neighbours[letter].add(lower_bound)

    lengths = {c: 0 for c in s}
    for letter in s:
        max_length = 0
        for neighbour in neighbours[letter]:
            if max_length < lengths[neighbour]:
                max_length = lengths[neighbour]
        lengths[letter] = max_length + 1

    return max(lengths.values())

print(longestIdealString("acfgbd", 2))
