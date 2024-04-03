#https://leetcode.com/problems/rotate-image/
def rotate(matrix):
    """
    This function rotates a given matrix 90 degrees clockwise in-place.

    :param matrix: A list of lists representing the matrix
    :return: None, the matrix is rotated in-place
    """
    # Initialize an empty list to store the rotated matrix
    result = []
    
    # Loop through the matrix columns
    for i in range(len(matrix)):
        # Initialize an empty list to store the current column
        o = []
        
        # Loop through the matrix rows in reverse order
        for j in range(len(matrix) - 1, -1, -1):
            # Add the current element to the current column
            o.append(matrix[j][i])
            
        # Add the current column to the rotated matrix
        result.append(o)
        
    # Clear the original matrix
    matrix.clear()
    
    # Add the rotated matrix columns to the original matrix
    for i in result:
        matrix.append(i)