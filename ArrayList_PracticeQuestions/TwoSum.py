nums = [1,4,3,5,6,8]
target = 10

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return(i,j)
            

print(two_sum(nums,target))


#Don't think the below one is correct method.
def two_sum_less_time(nums,target):
    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == target:
            return(i,i+1)
        
print(two_sum_less_time(nums,target))