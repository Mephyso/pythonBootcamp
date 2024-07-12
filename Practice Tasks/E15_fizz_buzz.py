"""
Create a python file named fizz_buzz, write a program that asks user to enter an integer and prints "Fizz" if the number is divisible by 3, prints "Buzz" if the number is divisible by 5, and prints FizzBuzz if the number is divisible by both 3 and 5.

            Ex:
                number 15

            Output:
                FizzBuzz
"""
number = int(input("Enter a number:"))
result = ""
if number%3 == 0:
    result += "Fizz"
if number%5 == 0:
    result += "Buzz"
print(result)