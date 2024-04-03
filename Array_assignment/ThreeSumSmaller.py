#https://leetcode.com/problems/3sum-smaller/ 
def three_sum_smaller(nums, target):
    # Sort the list
    nums.sort()

    # Initialize the result variable
    res = 0

    # Iterate through the list
    for i in range(len(nums)):
        # Initialize two pointers, j and k
        j, k = i + 1, len(nums) - 1

        # Loop while j is smaller than k
        while j < k:
            sum1 = nums[i] + nums[j] + nums[k]

            # If the sum is smaller than the target, increment the result
            # and move the left pointer to the right
            if sum1 < target:
                res += (k - j)
                j += 1

            # Otherwise, move the right pointer to the left
            else:
                k -= 1

    # Return the result
    return res