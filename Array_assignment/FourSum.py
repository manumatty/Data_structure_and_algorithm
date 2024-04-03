#https://leetcode.com/problems/4sum/
# Definition of the fourSum function, which takes a list of integers 'nums' and an integer 'target' as input
def fourSum(nums, target):
    # Sort the input list to allow for easier manipulation of the data
    nums.sort()

    # Initialize an empty list to store the results
    res = []

    # Initialize an empty list to store the unique answers
    ans = []

    # Iterate over the sorted list, starting from the first element and ending before the last three elements
    for i in range(len(nums) - 3):

        # Iterate over the sorted list, starting from the element after the current element and ending before the last two elements
        for j in range(i + 1, len(nums) - 1):

            # Initialize two pointers, one starting from the element after the current element and the other starting from the last element
            l = j + 1
            r = len(nums) - 1

            # Continue moving the pointers inward until they meet
            while l < r:

                # Calculate the sum of the four elements pointed to by i, j, l, and r
                current_sum = nums[i] + nums[j] + nums[l] + nums[r]

                # If the sum is equal to the target, append the four elements to the 'res' list
                if current_sum == target:
                    res.append((nums[i], nums[j], nums[l], nums[r]))

                    # Move the left pointer to the right to avoid duplicates
                    l += 1

                    # Move the right pointer to the left to avoid duplicates
                    r -= 1

                # If the sum is greater than the target, move the right pointer to the left
                elif current_sum > target:
                    r -= 1

                # If the sum is less than the target, move the left pointer to the right
                else:
                    l += 1

    # Convert the 'res' list to a set to remove any duplicates, and then convert it back to a list
    for i in list(set(res)):
        ans.append(list(i))

    # Return the 'ans' list as the final result
    return ans