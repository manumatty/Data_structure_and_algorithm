#https://leetcode.com/problems/contains-duplicate-ii/
# Function to check if there are any duplicate elements in the given list 'nums' within a window of size 'k'
def containsNearbyDuplicate(nums, k):
    # Initialize an empty dictionary 'dict1' to store the elements and their indices
    dict1 = {}
    
    # Iterate through the list 'nums' using the variable 'i'
    for i in range(0, len(nums)):
        # Check if the current element 'nums[i]' is already present in the dictionary 'dict1'
        if nums[i] in dict1.keys():
            # If the element is already present, return True as it indicates a duplicate within the window
            return True
        # If the element is not present, add it to the dictionary with a value of 1
        dict1[nums[i]] = 1
        # If the dictionary size exceeds 'k', remove the first element from the dictionary
        if(len(dict1) > k):
            dict1.pop(nums[i-k])
    # If no duplicates are found within the window, return False
    return False