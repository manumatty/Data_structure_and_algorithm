#https://leetcode.com/problems/contains-duplicate/
# Function to check if a list of numbers contains any duplicates
def containsDuplicate(nums):
    # Initialize an empty dictionary to store unique numbers
    list1 = {}
    
    # Iterate through the list of numbers
    for i in nums:
        # Check if the current number is already in the dictionary
        if i in list1.keys():
            # If the number is already in the dictionary, return True
            # as this indicates a duplicate has been found
            return True
        else:
            # If the number is not already in the dictionary,
            # add it to the dictionary with a value of 1
            list1[i] = 1
    
    # If no duplicates are found after iterating through the entire list,
    # return False
    return False