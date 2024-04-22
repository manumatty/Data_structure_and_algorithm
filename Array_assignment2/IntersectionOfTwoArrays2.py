#https://leetcode.com/problems/intersection-of-two-arrays-ii/
def intersect(nums1, nums2):
    # Initialize an empty dictionary 'dict1' to store unique elements from nums1
    dict1 = {}
    # Initialize an empty list 'res' to store the intersection of nums1 and nums2
    res = []

    # Populate dict1 with elements from nums1 as keys and their counts as values
    for i in nums1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    # Iterate through nums2, checking if each element is in dict1 and has a positive count
    for i in nums2:
        if i in dict1 and dict1[i] > 0:
            # If so, append the element to res and decrement its count in dict1
            res.append(i)
            dict1[i] -= 1

    # Return the list of intersecting elements
    return res