import heapq

def maximumToys(prices, k):
    heapq.heapify(prices)
    bought = 0
    for _ in range(len(prices)):
        k -= heapq.heappop(prices)
        if k < 0:
            break
        bought += 1
    return bought

print(maximumToys([3, 7, 2, 9, 4], 15))


