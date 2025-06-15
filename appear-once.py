def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out duplicate numbers
    return result

# Example usage
nums = [4, 1, 2, 1, 2]
print("Single number:", single_number(nums))  # Output: 4


# Find the element that appears only once (others appear twice)