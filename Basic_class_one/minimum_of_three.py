#we are providing solution to find minimum number from given three numbers
def minimum_of_three(num1,num2,num3):
    if num1 < num2:
        return min(num1,num3)
    else:
        return min(num2,num3)

