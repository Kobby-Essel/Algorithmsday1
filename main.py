"""
A program to determine if a number is an even number or odd number
"""
#function definition
def even_or_odd(value):
    x = int(value)
    if x%2==0:
        print("number is even")
    else:
        print("number is odd")

x = input("Enter a number\n")
#funtion call
even_or_odd(x)