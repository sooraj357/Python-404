def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Example usage
nums = [1, 1, 2, 2, 3]
length = remove_duplicates(nums)
print("After removing duplicates:", nums[:length])  # Output: [1, 2, 3]


# Remove duplicates in-place from a sorted array