"""
Create a python file named grade_level2.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

                    For Any Other grade: Invalid grade level given

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""
grade_level = int(input("Enter your grade level:"))
if 0 < grade_level <= 18:
    if grade_level <= 5:
        school_type = "Elementary school"
    elif grade_level <= 8:
        school_type = "Middle school"
    elif grade_level <= 12:
        school_type = "High school"
    elif grade_level <= 16:
        school_type = "College"
    else:
        school_type = "Grad School"
else:
    school_type = "Invalid Entry!"
print(school_type)