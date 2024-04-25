from collections import Counter
from itertools import chain


def maxLength(arr: list[str]) -> int:
        l=[set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            i = set(i)
            for j in l:
                if i & j:
                    continue
                l.append(i | j)
            print(l)
        m = 0
        for i in l:
            if m < len(i):
                m = len(i)
        return m


print(maxLength(["cha","r","act","ers"]))
