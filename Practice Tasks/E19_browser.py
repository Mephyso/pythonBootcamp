"""
Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if
"""
browser = input("Enter your browser name:")
if browser == "chrome" or browser == "firefox" or browser == "opera" or browser == "safari" or browser == "edge":
    if browser == "chrome":
        print("Chrome Browser is selected")
    if browser == "firefox":
        print("Firefox Browser is selected")
    if browser == "opera":
        print("Opera Browser is selected")
    if browser == "safari":
        print("Safari Browser is selected")
    if browser == "edge":
        print("Edge Browser is selected")
else:
    print("Invalid Browser Name")
