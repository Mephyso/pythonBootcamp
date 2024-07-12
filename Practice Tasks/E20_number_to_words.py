"""
Create a python file named number_to_words, Write a program that can convert user entered number (from 0~9) to words.

    NOTE: MUST use ternary

"""
number = int(input("Enter a number (0 to 9):"))
result = ""
result += "zero" if number == 0 else ""
result += "one" if number == 1 else ""
result += "two" if number == 2 else ""
result += "three" if number == 3 else ""
result += "four" if number == 4 else ""
result += "five" if number == 5 else ""
result += "six" if number == 6 else ""
result += "seven" if number == 7 else ""
result += "eight" if number == 8 else ""
result += "nine" if number == 9 else ""
if number < 0 or number > 9:
    result = "Invalid Entry!"
print(result)
