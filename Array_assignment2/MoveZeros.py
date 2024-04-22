#https://leetcode.com/problems/move-zeroes/
# Function: moveZeroes
# Description: This function takes a list of integers named 'nums' as input and rearranges its elements such that all the non-zero elements appear first,
#              followed by zero elements. The relative order of non-zero elements and zero elements remains unchanged.
def moveZeroes(nums):
    # Initialize two pointers, 'i' and 'j', both set to 0
    i = 0
    j = 0

    # Continue iterating through the list while 'j' is less than the length of the list 'nums'
    while j < len(nums):
        # If the current element at index 'j' is not equal to 0
        if nums[j]!= 0:
            # Swap the elements at indices 'i' and 'j'
            nums[i],nums[j]=nums[j],nums[i]
            # Increment 'i'
            i += 1
        # Increment 'j'
        j += 1