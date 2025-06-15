nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    lookup = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], index]
        lookup[num] = index
    return None

# Call the function *after* defining it
result = two_sum(nums, target)
print("Indices:", result)


# Find indices of two numbers that add up to a target
