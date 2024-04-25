from collections import defaultdict
import math

def countSubarrays( nums: list[int], minK: int, maxK: int) -> int:
    index_min = index_max = None
    count = start = 0
    for i, num in enumerate(nums):
        # num is outside the bounds so we "reset", carrying our count from the next index
        if not(minK <= num <= maxK):
            index_min = index_max = None
            start = i + 1
            continue
        if num == minK:
            index_min = i
        if num == maxK:
            index_max = i
        # both minK and maxK are present, so we update count:
        # - the first one to appear indicates how many permutations we need to add
        # - start is an offset to the part of the array we are currently working with
        if index_min is not None and index_max is not None:
            count += min(index_min, index_max) - start + 1
    return count


