from collections import defaultdict
def subarraysWithKDistinct(nums: list[int], k: int) -> int:
    def subarraysWithAtMostK(nums: list[int], k: int) -> int:
        counter = defaultdict(int)
        l = r = count = 0

        while r < len(nums):
            counter[nums[r]] += 1
            while len(counter.keys()) > k:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1
            if len(counter.keys()) <= k:
                count += r - l + 1
            r += 1
        return count

    return subarraysWithAtMostK(nums, k) - subarraysWithAtMostK(nums, k-1)

print(subarraysWithKDistinct([1,2,1,2,3], 2))
print(subarraysWithKDistinct([1,2,1,3,4], 3))