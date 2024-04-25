import heapq
from math import prod


def maximumProduct(nums: list[int], k: int) -> int:
    heapq.heapify(nums)
    while k > 0:
        heapq.heapreplace(nums, nums[0]+1)
        k -= 1
    return prod(nums) % (10 ** 9 + 7)


print(maximumProduct([9, 7, 8], 9))
