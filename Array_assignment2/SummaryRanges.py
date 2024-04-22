#https://leetcode.com/problems/summary-ranges/
def summaryRanges(nums):
        # Initialize an empty list to store the ranges
        res=[]

        # If the input list is empty, return the empty list
        if(len(nums)==0):
            return res

        # Initialize start and end indices for the current range
        start=0
        end=0

        # Iterate through the input list, comparing each element to the previous one
        for i in range(1,len(nums)):
            # If the current element is not consecutive with the previous one,
            # update the end index of the current range and append the range
            # to the result list
            if(nums[i]!=nums[i-1]+1):
                end=i-1
                if start==end:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start])+"->"+str(nums[end]))
                # Update the start index to the current index
                start=end=i

        # Handle the last range in the input list
        end=len(nums)-1
        if(start==end):
            res.append(str(nums[start]));
        else:
            res.append(str(nums[start])+"->"+str(nums[end]))

        # Return the list of ranges
        return res