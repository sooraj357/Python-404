def move_zeroes(nums):
    i = 0  # Pointer for the next non-zero position
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

# Example usage
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print("After moving zeros:", nums)  # Output: [1, 3, 12, 0, 0]


# Move all 0s to the end while maintaining the order of non-zero elements