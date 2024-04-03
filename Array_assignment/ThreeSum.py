#https://leetcode.com/problems/3sum/description/
def threeSum(nums):
    """
    This function takes a list of integers as an input and returns a list of lists, where each sublist contains three integers
    from the original list that add up to zero.

    The function uses a brute-force approach with a nested while loop to find all possible combinations of three integers that
    add up to zero. The function first sorts the input list to optimize the inner while loop and eliminate duplicate combinations.
    The function uses two pointers, a start pointer and an end pointer, to iterate through the sorted list and find all possible
    combinations of three integers that add up to zero.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    :param nums: list of integers
    :return: list of lists of three integers that add up to zero
    """
    res = []  # initialize an empty list to store the final result
    nums.sort()  # sort the input list to optimize the inner while loop

    for i in range(len(nums) - 2):  # outer for loop to iterate through the input list

        if i > 0 and nums[i] == nums[i - 1]:  # check if the current integer is the same as the previous integer
            continue  # if so, skip the current integer and move to the next iteration

        start = i + 1  # initialize the start pointer
        last = len(nums) - 1  # initialize the end pointer

        while start < last:  # inner while loop to find all possible combinations of three integers that add up to zero

            if start > i + 1 and nums[start] == nums[start - 1]:  # check if the current integer is the same as the previous integer
                start += 1  # if so, skip the current integer and move to the next integer

            sum1 = nums[i] + nums[start] + nums[last]  # calculate the sum of the three integers

            if sum1 == 0:  # if the sum of the three integers is zero
                res.append([nums[i], nums[last], nums[start]])  # append the three integers to the final result
                start += 1  # move the start pointer to the next integer
                last -= 1  # move the end pointer to the previous integer

            elif sum1 > 0:  # if the sum of the three integers is greater than zero
                last -= 1  # move the end pointer to the previous integer

            else:  # if the sum of the three integers is less than zero
                start += 1  # move the start pointer to the next integer

    return res  # return the final result