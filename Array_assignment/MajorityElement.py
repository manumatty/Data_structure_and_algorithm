#https://leetcode.com/problems/majority-element/
def majorityElement(nums):
    """
    This function returns the majority element in a list.
    A majority element is an element that appears more than n/2 times in a list of size n.
    The algorithm to find the majority element is based on the Boyer-Moore vote algorithm.

    Parameters:
    nums (list): A list of integers

    Returns:
    int: The majority element in the list
    """
    maj = nums[0]  # Initialize the majority element as the first element of the list
    count = 1     # Initialize the count of the majority element as 1

    for i in nums:
        # If the current element is equal to the majority element, increment the count
        if i == maj:
            count += 1
        # If the current element is not equal to the majority element, decrement the count
        else:
            count -= 1
        # If the count becomes zero, update the majority element as the current element and reset the count to 1
        if count == 0:
            maj = i
            count = 1

    return maj