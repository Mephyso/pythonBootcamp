age = 40
name = "Adil"
print("This is " + "one String")    # -----> This is one String
# print("This is " + 5) -------> Error
print("This is " + str(5))     # ---------> This is 5

print(int("5")+5)   # This is not concatenation, this is addition

print("My age is {}".format(age))
print(f"My age is {age}")

print("My name is {} and I am {} years old.".format("Ömer",age))
print(f"My name is {name} and I am {age-35} years old.")

print("This is ", "one String")
print("This is ", 5, ". Is it ", True,"?")
