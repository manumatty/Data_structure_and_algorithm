#https://leetcode.com/problems/merge-sorted-array/ 
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
   """
   This function merges two sorted arrays (nums1 and nums2) into a single sorted array in-place within nums1.

   :param nums1: The first sorted array, which will be modified in-place to contain the merged sorted array.
   :param m: The length of the first array (nums1).
   :param nums2: The second sorted array.
   :param n: The length of the second array (nums2).
   """
   last = len(nums1) - 1  # Initialize a variable 'last' to keep track of the last index of nums1

   # Iterate as long as there are remaining elements in both arrays
   while m > 0 and n > 0:
       if nums2[n - 1] >= nums1[m - 1]:  # If the current element in nums2 is greater than or equal to the current element in nums1
           nums1[last] = nums2[n - 1]  # Move the current element from nums2 to the end of nums1
           n -= 1  # Decrease the counter for nums2
       else:  # Otherwise
           nums1[last] = nums1[m - 1]  # Move the current element from nums1 to the end of nums1
           m -= 1  # Decrease the counter for nums1
       last -= 1  # Decrease the 'last' index to move to the next position in nums1

   # If there are remaining elements in nums2, move them to the beginning of nums1
   while n > 0:
       nums1[last] = nums2[n - 1]
       n -= 1
       last -= 1 