#https://leetcode.com/problems/pascals-triangle/description/
# Function to generate Pascal's Triangle up to a given number of rows
def generate(numRows):
   # Initialize an empty list to store the rows of the triangle
   result = []
   
   # If the user requests 0 rows, return an empty list
   if numRows == 0:
       return result
   
   # Add the first row of the triangle (only 1 element, 1)
   result.append([1])
   
   # Iterate through the remaining rows to be generated
   for i in range(1, numRows):
       # Create a new row with the first element as 1
       newRow = [1]
       
       # Get the previous row to calculate the next row
       prevRow = result[i-1]
       
       # Iterate through the elements of the previous row (except the last one)
       for j in range(1, len(prevRow)):
           # Calculate the new element by adding the previous and current elements
           newRow.append(prevRow[j-1] + prevRow[j])
       
       # Add the last element (1) to the new row
       newRow.append(1)
       
       # Append the new row to the triangle
       result.append(newRow)
   
   # Return the generated triangle
   return result