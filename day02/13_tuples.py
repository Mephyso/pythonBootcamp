days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
irregular = 1.1, 2.2, 3.3, True, False, True, "Modern", "Art", 3, 5, 7

work_days = days[:5]
print(days)
print(work_days)

"""
           0         1          2             3         4           5         6       forward index
days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
          -7        -6         -5            -4        -3           -2       -1       backward index
"""

arguments = irregular[3:6]
print(arguments)
strings = irregular[-5:-3]
print(strings)
decimals = irregular[:3]
print(decimals)
weekend = days[5:]
print(weekend)


print(len(days), days)
print(len(irregular), irregular)

"""
days[1] = "Today"   ------>   TypeError: 'tuple' object does not support item assignment
"""

days_backward = days[::-1]
print(days_backward)

t1 = 1, "2", 3
t2 = 1, "2", 3

print(t1 is t2)
print(t1 == t2)

t1 = 1, 2, 3
t2 = 4, 5
t3 = t1 + t2
t4 = t1 * 4
print(t3, t4)
print(tuple(reversed(t3)))

answers = "a", "b", "a", "a", "d", "b", "c", "e"
print(answers, "index of e", answers.index("e"))
print(answers, " count of a", answers.count("a"))

counter = 0
for choices in answers:
    counter += 1
    print(counter, choices)

irregular_nested = ((1.1, 2.2, 3.3), (True, False, True), ("Modern", "Art"), (3, 5, 7))
print(irregular_nested)
