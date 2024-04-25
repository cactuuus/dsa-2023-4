import heapq
from collections import defaultdict


def largestPermutation(k, arr):
    values_left = [(-value, -index) for index, value in enumerate(arr)]
    heapq.heapify(values_left)

    swaps = i = 0
    while swaps < k and i < len(arr):
        while values_left and -values_left[0][1] <= i:
            heapq.heappop(values_left)
        if values_left and -values_left[0][0] > arr[i]:
            value, max_index = heapq.heappop(values_left)
            heapq.heappush(values_left, (-arr[i], max_index))
            arr[i], arr[-max_index] = -value, arr[i]
            swaps += 1
        i += 1

    return arr


print(largestPermutation(200, [1]))
