# two pointers approach

def two_sum(nums, target):

    if not nums:
        raise ValueError("Input list cannot be empty")

    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [nums[left], nums[right]]
        
        elif total < target:
            left += 1
        
        else:
            right-= 1
    
    return []
        
