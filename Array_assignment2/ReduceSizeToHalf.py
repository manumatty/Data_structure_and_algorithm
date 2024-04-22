#https://leetcode.com/problems/reduce-array-size-to-the-half/
def minSetSize(arr):
    # Initialize a frequency bucket to store the count of each element in the array
    bucket = [0] * 100001

    # Iterate through the array and update the frequency bucket
    for i in arr:
        bucket[i] += 1

    # Sort the frequency bucket in descending order
    bucket.sort(reverse=True)

    # Initialize variables to keep track of the minimum set size and the total elements
    k = 0
    total = len(arr)

    # Iterate through the frequency bucket in reverse order
    for i in range(len(bucket) - 1, -1, -1):
        # Subtract the count of the current element from the total elements
        total -= bucket[i]

        # Increment the minimum set size
        k += 1

        # If the total elements is less than or equal to half of the array length, break the loop
        if total <= len(arr) // 2:
            break

    # Return the minimum set size
    return k