alphacount = 0
spacecount = 0
count = 0
for char in "talisman of reality1":
    if char.isalpha():
        alphacount += 1
    elif char == " ":
        spacecount += 1
    else:
        count += 1
print(f"There is {alphacount} alphabetical characters {spacecount} spaces and {count} other characters in this string")


print("----------------------------------------------------------")
print("These are odd numbers 0 to 10:")
for i in range(1, 11):
    if i % 2 == 1:
        print(i)

print("----------------------------------------------------------")
print("These are odd numbers 10 to 0:")
for i in reversed(range(1, 11)):
    if i % 2 == 1:
        print(i)

print("----------------------------------------------------------")
n = int(input("Give me a negative number: "))
while n >= 0:
    n = int(input("Give me a negative number: "))
print(f"You did it! You gave me {n}! ")

print("----------------------------------------------------------")
answer = input("Long or short ? ")
while not (answer.lower() == "short" or answer.lower() == "long"):
    answer = input("Long or short ? ")
print(f"Correct, it is really so {answer.lower()}!")

print("----------------------------------------------------------")
print("These are odd numbers 0 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # skips to the next iteration
    print(i)

print("----------------------------------------------------------")
print("These are odd numbers until 6:")
for i in range(1, 11):
    if i == 6:
        break       # exits the loop
    if i % 2 == 0:
        continue    # skips to the next iteration
    print(i)


print("----------------------------------------------------------")
print("These are odd numbers until 10:")
for i in range(1, 11):
    if i == 6:
        pass       # I am planning doing something but yet I don't know what I have to do
    if i % 2 == 0:
        pass        # I am planning doing something but yet I don't know what I have to do


def function():
    pass


if True:
    pass


class Class:

    def method(self):
        pass

    pass
