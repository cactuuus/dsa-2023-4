def searchInsert(nums: list[int], target: int) -> int:
    if len(nums) == 1:
        return 0 if target < nums[0] else 1
    
    i = len(nums) // 2
    if nums[i-1] > target:
        i = searchInsert(nums[:i], target)
    elif nums[i] < target:
        i += searchInsert(nums[i:], target)

    return i


print(searchInsert([1,3,5,6], 0))