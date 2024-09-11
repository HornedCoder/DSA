def duplicates(nums):
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            return True
        
    return False



nums = [0]

print(duplicates(nums))