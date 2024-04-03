#https://leetcode.com/problems/missing-ranges/ 
# Definition of the function with input parameters
# nums: a list of integers, representing the sorted array of numbers
# lower: an integer, representing the lower bound of the range
# upper: an integer, representing the upper bound of the range
def findMissingRanges(nums, lower, upper):
    # Check if the input list is empty
    if not nums:
        # If the list is empty, return None
        return None
    
    # Initialize an empty list to store the missing ranges
    result=[]

    # Iterate through the input list
    for i in nums:
        # Check if the current number is less than the lower bound
        if i< lower:
            # If it is, continue to the next iteration
            continue
        # Check if the current number is equal to the lower bound
        if i == lower:
            # If it is, increment the lower bound by 1
            lower +=1
            # Continue to the next iteration
            continue

        # Check if the lower bound is equal to the current number minus 1
        if(lower == i-1):
            # If it is, append the lower bound as a string to the result list
            result.append(str(lower))
        else:
            # If it is not, append a string representation of the range from the lower bound to the current number minus 1
            result.append(str(lower)+"->"+str(i-1))
        # Increment the lower bound by the current number plus 1
        lower=i+1
    
    # Check if the upper bound is equal to the lower bound
    if upper == lower:
        # If it is, append the upper bound as a string to the result list
        result.append(str(upper))
    elif(upper-lower>1):
        # If it is not, and the difference between the upper and lower bounds is greater than 1, append a string representation of the range from the lower bound to the upper bound
        result.append(str(lower)+"->"+str(upper))
    # Return the list of missing ranges
    return result