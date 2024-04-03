#https://leetcode.com/problems/majority-element-ii/
def majorityElement(nums):   # Takes a list of numbers as input and returns the majority elements in the list
    c1 = c2 = e1 = e2 = 0  # Initialize counters and majority elements
    for i in nums:          # Iterate over the list of numbers
        if e1 == i:       # If the first majority element is equal to the current number
            c1 += 1       # Increment the counter for the first majority element
        elif e2 == i:     # If the second majority element is equal to the current number
            c2 += 1       # Increment the counter for the second majority element
        elif c1 == 0:    # If the counter for the first majority element is 0
            e1 = i       # Set the first majority element to the current number
            c1 = 1       # Reset the counter for the first majority element to 1
        elif c2 == 0:    # If the counter for the second majority element is 0
            e2 = i       # Set the second majority element to the current number
            c2 = 1       # Reset the counter for the second majority element to 1
        else:           # If neither of the above conditions are met
            c1 -= 1      # Decrement the counter for the first majority element
            c2 -= 1      # Decrement the counter for the second majority element

    c1 = c2 = 0        # Reset the counters
    for i in nums:      # Iterate over the list of numbers again
        if i == e1:     # If the current number is equal to the first majority element
            c1 += 1     # Increment the counter for the first majority element
        elif i == e2:   # If the current number is equal to the second majority element
            c2 += 1     # Increment the counter for the second majority element

    result = []        # Initialize a list to store the majority elements
    if c1 > len(nums) // 3:    # If the counter for the first majority element is greater than a third of the list length
        result.append(e1)     # Add the first majority element to the result list
    if c2 > len(nums) // 3:    # If the counter for the second majority element is greater than a third of the list length
        result.append(e2)     # Add the second majority element to the result list

    return result       # Return the result list