#Solution to return midean value of given three numbers
def mid_of_three(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            return num2
        else:
            return num3
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num1 > num2:
            return num1
        else:
            return num2

