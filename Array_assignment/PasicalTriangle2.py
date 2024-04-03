#https://leetcode.com/problems/pascals-triangle-ii/
# Function to get row of Pascal's Triangle
def getRow(rowIndex):
   # Initialize the result list with first element (1)
   res = [1]
   # If rowIndex is 0, return the result list
   if rowIndex == 0:
       return res

   # Generate the Pascal's Triangle row
   for i in range(1, rowIndex + 1):
       # Initialize a new row with the first element (1)
       newRow = [1]
       # Calculate the inner elements of the row
       for j in range(1, i):
           # Add the previous two elements in the previous row
           newRow.append(res[j - 1] + res[j])
       # Add the last element (1) to the new row
       newRow.append(1)
       # Replace the current result list with the new row
       res = newRow

   # Return the final result list
   return res