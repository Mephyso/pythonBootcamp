score = 75
if score < 50:
    print("Your note is F")
    Note = "F"
elif score < 60:
    print("Your note is E")
    Note = "E"
elif score < 70:
    print("Your note is D")
    Note = "D"
elif score < 80:
    print("Your note is C")
    Note = "C"
elif score < 90:
    pass
    #   print("Your note is B")
else:
    print("Your note is A")
    Note = "A"


result = 5
result = 4 if Note == "A" else print(result)
print(result)
# You must give a proper value to variable (result). When you dont attend any value, variable (result) equals "None"
'''
result = 3 if Note == "B" else print(result)
result = 2 if Note == "C" else print(result)
result = 1 if Note == "D" else print(result)
result = 0.5 if Note == "E" else print(result)
result = 0 if Note == "F" else print(result)
'''

score = 105
if 0 <= score <= 100:
    if score >= 60:
        print("Passed")
    else:
        print("Failed")
else:
    print("invalid entry")
