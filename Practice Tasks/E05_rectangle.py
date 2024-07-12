"""
Create a python file named Rectangle, write a program that can calculate the area & perimeter of any given Rectangle

        Hint: width and length need to be given to calculate the area and perimeter of rectangle
            Ex:
                Given Data:
                    length = 5
                    width = 2

                output:
                    Area of the rectangle is equal to 10
                    Perimeter of rectangle is equal to 14
"""
length = int(input("What is the length of Rectangle:"))
width = int(input("What is the width of Rectangle:"))
print("Area of the square is equal to ", length*width)
print("Perimeter of square is equal to ", (length+width)*2)