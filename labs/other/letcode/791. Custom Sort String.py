from collections import Counter
def customSortString(order: str, s: str) -> str:
    counter = Counter(s)
    output = ""
    for letter in order:
        output += letter * counter.pop(letter, 0)
    for leftover in counter:
        output += leftover * counter.get(leftover)
    return output

print(customSortString("bcafg", "abcd"))