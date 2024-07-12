code = "python"
'''
index order of strings in python:
    0  1  2  3  4  5
    p  y  t  h  o  n
   -6 -5 -4 -3 -2 -1
'''
print(code[0]+code[-5])     # ----> py
length = len(code)          # ----> 6 (length of the string)
print(code[-len(code)]+code[len(code)-1])     # ----> pn

s1 = code[0:3]      # ----> pyt
s2 = code[:3]       # ----> pyt
s3 = code[3:]       # ----> hon
print(code, s1, s2, s3, s2+s3)

s4 = code[::2]      # ----> pto (take every next 2. character)
print(s4)
s4 = code[::3]      # ----> ph (take every next 3. character)
print(s4)
s4 = code[::1]      # ----> python (take every next 1. character)
print(s4)
s4 = code[::-1]     # ----> nohtyp (take every next 1. character backward)
print(s4)
s4 = code[::-2]     # ----> nhy (take every next 2. character backward)
print(s4)

code = "that is an order of sequence"
print(code.upper())             # ----> THAT IS AN ORDER OF SEQUENCE
print(code.upper().isupper())   # ----> True
print(code.lower())             # ----> that is an order of sequence
print(code.lower().islower())   # ----> True
print(code.capitalize())        # ----> That is an order of sequence
print(code.capitalize()[0].isupper())   # ----> True
print(code.capitalize()[0].islower())   # ----> False
print(code.title())             # ----> That Is An Order Of Sequence

code = " d e n e m e "
print(code.strip())         # ----> d e n e m e (no more white space before and after string)
print(code.index("e"))      # ----> 3  (index of first "e" in the string)
# print(code.index("r"))    # ----> ValueError: substring not found
print(code.rindex("e"))     # ----> 11 (index of last "e" in the string)
# print(code.rindex("r"))   # ----> ValueError: substring not found

code = "Panama"
print(code.replace("a","i"))                # Panama ----> Pinimi (find and replace first string with second string)
print(code.replace("a","i", 2))     # Panama ----> Pinima (find and replace 2 (count) of first string with second string)
print((code.count("a")))                                # ----> 3

code = "JavA01 PytHon2 ScrIpt30O"
print(code.swapcase())         # JavA01 PytHon2 ScrIpt30O ----> jAVa01 pYThON2 sCRiPT30o
print(code[4].isdigit())       # ----> True
print(code[0].isdigit())       # ----> False
print(code[0].isalpha())       # ----> True
print("Java Python Script".istitle())          # ----> True
print("JavA PytHon ScriPt".istitle())          # ----> False