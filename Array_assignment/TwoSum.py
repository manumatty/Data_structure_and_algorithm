#https://leetcode.com/problems/two-sum/description/
'''This is the optimistic way of solving two sum problem
The Space complexity is O(n)
The time Complexity is also O(n)'''
def twoSum(nums, target) :
        dict1={}
        for i in range(0,len(nums)):
            if target-nums[i] in dict1:
                return [dict1[target-nums[i]],i]
            else:
                dict1[nums[i]]=i
        return []
