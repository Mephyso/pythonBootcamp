"""
Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            other wise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
grade = input("Enter your grade (A to F):")
if "A" <= grade <= "F":
    if grade == 'A':
        result = "Excellent"
    elif grade == 'B':
        result = "Great job"
    elif grade == 'C':
        result = "Good"
    elif grade == 'D':
        result = "Passed"
    else:
        result = "Failed"
else:
    result = "Invalid Entry!"
print(result)