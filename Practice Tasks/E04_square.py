"""
Create a python file named Square, write a program that can calculate the area & perimeter of any given square

        Hint: side need to be given to calculate the area and perimeter of square
            Ex:
                Given Data:
                    side = 5

                output:
                    Area of the square is equal to 25
                    Perimeter of square is equal to 20
"""
side = int(input("What is the length of one side:"))
print("Area of the square is equal to ", side*side)
print("Perimeter of square is equal to ", side*4)