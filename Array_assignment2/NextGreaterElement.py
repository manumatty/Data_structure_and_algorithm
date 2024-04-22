#https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(nums1, nums2):
    # Initialize an empty dictionary and result list
    dict1 = {}
    res = []

    # Initialize an empty stack
    stack = []

    # Iterate over nums2
    for num in nums2:
        # While the stack is not empty and the top element of the stack is less than the current number
        while len(stack) > 0 and stack[-1] < num:
            # Add the top element of the stack and its corresponding greater number to the dictionary
            dict1[stack.pop()] = num
        # Add the current number to the stack
        stack.append(num)

    # Initialize the result list with -1 for each element in nums1
    res = [-1] * len(nums1)

    # Iterate over nums1
    for i in range(len(nums1)):
        # If the current number in nums1 is in the dictionary
        if nums1[i] in dict1.keys():
            # Add the corresponding greater number to the result list
            res[i] = dict1[nums1[i]]

    # Return the result list
    return res