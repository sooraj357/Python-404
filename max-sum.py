def max_sub_array(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_sub_array(nums)
print("Maximum subarray sum:", result)  # Output: 6


# Find the contiguous subarray with maximum sum (Kadane’s Algorithm)