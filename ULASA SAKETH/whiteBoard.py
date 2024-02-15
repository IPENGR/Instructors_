def decimal_to_octal(decimal):
    #if the decimal is equals to zero it will return empty string
    if decimal == 0:
        return ""
    #calculating the quotient and reminder when the decimal number is divided by 8
    quotient=decimal // 8
    remainder=decimal % 8
    #calling the function with a quotient and concatinate with reminder as a string
    return decimal_to_octal(quotient)+str(remainder)
#taking input from user
decimal=int(input("enter the decimal number :"))
#calling the function to convert decimal to octal
octal=decimal_to_octal(decimal)
#printing the result
print("octal number is",octal,"for", decimal)