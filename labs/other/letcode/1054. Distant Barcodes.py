import heapq
from collections import Counter
def rearrangeBarcodes(barcodes: list[int]) -> list[int]:
    heap = [(-v, k) for k, v in Counter(barcodes).items()]
    heapq.heapify(heap)
    output = []
    for _ in range(len(barcodes)):
        k, v = heapq.heappop(heap)
        output.append(v)
        heapq.heappush(heap, (k+1, v))
    return output

print(rearrangeBarcodes([1,1,1,2,2,2]))