def isValid(s: str) -> bool:
    count = dict.fromkeys("abc", 0)
    for c in s:
        count[c] += 1
        if count["c"] > count["b"] or count["b"] > count["a"]:
            return False
    return True

print(isValid("abccba"))