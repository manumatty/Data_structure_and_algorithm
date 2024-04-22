#https://leetcode.com/problems/intersection-of-two-arrays/
def intersection(nums1, nums2):
    # Sort both input lists to enable efficient comparison of elements
    nums1.sort()
    nums2.sort()

    # Initialize an empty list to store the intersection of the two lists
    res = []

    # Initialize two indices for traversing the sorted lists
    i = j = 0

    # Continue iterating while the indices are within the list bounds
    while i < len(nums1) and j < len(nums2):
        # Skip duplicate elements in the first list to avoid redundant comparisons
        if i!= 0 and nums1[i] == nums1[i - 1]:
            i += 1
            continue

        # Skip duplicate elements in the second list to avoid redundant comparisons
        if j!= 0 and nums2[j] == nums2[j - 1]:
            j += 1
            continue

        # If the current elements in both lists are equal, add the element to the result list
        # and increment both indices
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1

        # If the current element in the first list is greater, increment the index of the second list
        elif nums1[i] > nums2[j]:
            j += 1

        # Otherwise, increment the index of the first list
        else:
            i += 1

    # Return the list containing the intersection of the two input lists
    return res