# Python Program to Check if a Number is Odd or Even

n = int(input("Enter a number:"))
if n%2 == 0:
    print("Even number")
else:
    print("odd number")


def check(n):
    if n < 2:
        return(n % 2 == 0)
    return (check(n-2))















