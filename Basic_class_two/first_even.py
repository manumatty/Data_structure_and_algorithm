#program to return first even number in array otherwise -1
def first_even(arr1):
    result=-1
    for i in arr1:
        if i%2 == 0: # logic to find even number
            result=i
            break
    return result

