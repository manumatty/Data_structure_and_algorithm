#https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    # Constructor that initializes the array 'res' with the cumulative sum of the input nums list
    def __init__(self, nums: List[int]):
        self.res = [0] * len(nums)
        self.res[0] = nums[0]
        for i in range(1, len(nums)):
            self.res[i] = self.res[i-1] + nums[i]

    # Function to calculate the sum of the elements from 'left' to 'right' indices in the input nums list
    def sumRange(self, left: int, right: int) -> int:
        # If the left index is 0, return the cumulative sum up to the right index
        if left == 0:
            return self.res[right]
        # Otherwise, return the difference between the cumulative sum up to the right index and the cumulative sum up to the left index
        else:
            return self.res[right] - self.res[left-1]