#https://leetcode.com/problems/3sum-closest/
def threeSumClosest(nums, target):
    # Initialize the result and the minimum difference variable diff
    result=0
    diff=float('inf')

    # Sort the input list
    nums.sort()

    # Iterate through the sorted list
    for i in range(len(nums)):

        # Initialize start and end pointers for the two sum problem
        start=i+1
        end=len(nums)-1

        # Continue with the two sum problem while the start pointer is less than the end pointer
        while(start < end):

            # Calculate the sum of the three numbers (current number + start number + end number)
            sum1=nums[i]+nums[start]+nums[end]

            # If the absolute difference between the sum and the target is less than the current minimum difference,
            # update the minimum difference and the result
            if(diff>abs(sum1-target)):
                diff=abs(sum1-target)
                result=sum1

            # If the sum is greater than the target, move the end pointer to the left
            if sum1-target>0:
                end -=1

            # If the sum is less than the target, move the start pointer to the right
            elif sum1-target<0:
                start+=1

            # If the sum is equal to the target, return the sum as the result
            else:
                return sum1

    # Return the result after all iterations
    return result