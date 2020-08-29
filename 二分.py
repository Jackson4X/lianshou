def findMin(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right + 1) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot +1
    return -1

nums = [5]
num = findMin(nums, 5)
print(num)