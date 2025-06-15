def remove_element(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Example usage
nums = [3, 2, 2, 3, 4]
val = 3
length = remove_element(nums, val)
print("After removing", val, ":", nums[:length])  # Output: [2, 2, 4]


# Remove all instances of a given value in-place