from collections import Counter

def beautifulPairs(A, B):
    """
    params: A: a list of integers of size n
    params: B: a list of integers of size n
    """
    pairs = (Counter(A) & Counter(B)).total()
    print(Counter(A) & Counter(B))
    if pairs == len(A):
        return pairs - 1
    else:
        return pairs + 1


print(beautifulPairs([1,2,3,4,5], [5,4,3,2,2]))