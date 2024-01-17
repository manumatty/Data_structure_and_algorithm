#To find all odd numbers in array
def odd_num(arr):
    result=[]
    for i in arr:
        if i % 2 != 0:#logic for odd number
            result.append(i)
    return result

