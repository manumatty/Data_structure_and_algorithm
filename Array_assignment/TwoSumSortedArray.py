# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Function to find the indices of two numbers in an array that add up to a given target value
def twoSum(numbers, target) :
   # Initialize left and right pointers at the beginning and end of the array respectively
   left = 0
   right = len(numbers) - 1

   # Continue the search until the left pointer's value plus the right pointer's value equals the target
   while (numbers[left] + numbers[right] != target):
       # If the sum is greater than the target, move the right pointer towards the left
       if (numbers[left] + numbers[right] > target):
           right = right - 1
       # If the sum is less than the target, move the left pointer towards the right
       else:
           left = left + 1

   # Return a list containing the indices of the two numbers that add up to the target
   return [left + 1, right + 1]