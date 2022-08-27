def sum_numbers(*nums):
    total_items = len(nums)
    result = 0
    for i in range(total_items):
        result += nums[i]
    return result


new_result = sum_numbers(12, 60,45)
print(new_result)
