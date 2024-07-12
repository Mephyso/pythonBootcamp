"""
import tools

print(tools.summ(2))
print(tools.summ(2, 5))
print(tools.summ(2, 5, 7))

import tools as t

print(t.summ(2))
print(t.summ(2, 5))
print(t.summ(2, 5, 7))

"""

from tools import summ

print(summ(2))
print(summ(2, 5))
print(summ(2, 5, 7))

from tools import divide as div

print(div(5, 2))
