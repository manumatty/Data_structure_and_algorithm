#https://leetcode.com/problems/next-greater-element-ii/
def nextGreaterElements(nums):
    # Initialize result list with -1 as default value
    res = [-1] * len(nums)
    
    # Create an empty list to store the indices of the numbers in the 'nums' list
    great = []
    
    # Iterate through the 'nums' list twice to find the next greater element for each number
    for i in range(len(nums) * 2):
        # Get the current number and its index
        num = nums[i % len(nums)]
        index = i % len(nums)
        
        # While there are elements in the 'great' list and the last element is smaller than the current number,
        # update the result list with the current number and remove the last element from the 'great' list
        while len(great) > 0 and nums[great[-1]] < num:
            res[great.pop()] = num
            
        # If we are still iterating through the 'nums' list, add the current index to the 'great' list
        if i < len(nums):
            great.append(index)
            
    # Return the result list
    return res