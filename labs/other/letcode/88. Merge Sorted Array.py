class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return nums1

        j = 0
        for i in range(m):
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
            else:
                j += 1

        for i in range(n):
            nums1[m+i] = nums2[i]