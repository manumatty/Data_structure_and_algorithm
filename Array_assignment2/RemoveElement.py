#https://leetcode.com/problems/remove-element/
def removeElement(nums, val):
    # Initialize a result variable to keep track of the number of elements to be kept in the array
    res = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is not equal to the value to be removed
        if nums[i]!= val:
            # Replace the element at the res index with the current element
            nums[res] = nums[i]
            # Increment the res variable
            res += 1

    # Return the number of elements to be kept in the array
    return res