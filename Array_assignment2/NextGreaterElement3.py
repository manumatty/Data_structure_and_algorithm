#https://leetcode.com/problems/next-greater-element-iii/
def nextGreaterElement(n):
    """
    This function returns the next greater element of a given positive integer.
    If no such element exists, it returns -1.
    
    :param n: A positive integer
    :return: The next greater element or -1 if no such element exists
    """
    ele = list(str(n))  # Convert the integer to a list of characters
    i = len(ele) - 1  # Initialize the index to the last element

    # Find the first element that is smaller than its next element
    while i > 0 and ele[i - 1] >= ele[i]:
        i -= 1

    # If no such element is found, return -1
    if i == 0:
        return -1

    # Find the smallest element greater than the element found above
    smallIndex = i
    x = ele[i - 1]
    for j in range(i + 1, len(ele)):
        if ele[j] > x and ele[j] <= ele[smallIndex]:
            smallIndex = j

    # Swap the found element with the smallest greater element
    ele[i - 1], ele[smallIndex] = ele[smallIndex], ele[i - 1]

    # Sort the remaining elements in ascending order
    ele[i:] = sorted(ele[i:])

    # Convert the list back to an integer
    res = int(''.join(ele))

    # Check if the result is within the range of a 32-bit signed integer
    return res if res <= 2**31-1 else -1