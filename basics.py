# Variables are dynamicly typed
n = 0
print('n =', n)
>>> n = 0
#check
n = "abc"
print('n =', n)
>>> n = abc

# Multiple assignments
n, m = 0, "abc"
n, m, z = 0.125, "abc", False

# Increment
n = n + 1 # good
n += 1    # good
n++       # bad

# None is null (absence of value)
n = 4
n = None
print("n =", n)
>>> n = None

# If statements don't need parentheses 
# or curly braces.
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multi-line conditions.
# and = &&
# or  = ||
n, m = 1, 2
if ((n > 2 and 
    n != m) or n == m):
    n += 1
n = 0
while n < 5:
    print(n)
    n += 1
>>> 0 1 2 3 4

# Looping from i = 0 to i = 4
for i in range(5):
    print(i)
>>> 0 1 2 3 4

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)
>>> 2 3 4 5

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)
>>> 5 4 3 2
    
# Division is decimal by default
print(5 / 2)
>>> 2.5

# Double slash rounds down
print(5 // 2)
>>> 2

# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
print(-3 // 2)
>>> -2

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
print(int(-3 / 2))
>>> -1

# Modding is similar to most languages
print(10 % 3)
>>> 1

# Except for negative values
print(-10 % 3)
>>> 2

# To be consistent with other languages modulo
import math
from multiprocessing import heap
print(math.fmod(-10, 3))
>>> -1

# More math helpers
print(math.floor(3 / 2))
>>> 1
print(math.ceil(3 / 2))
>>> 2
print(math.sqrt(2))
>>> 1.4142135623730951
print(math.pow(2, 3))
>>> 8

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))
>>> 1.6069380442589903e+60

# But still less than infinity
print(math.pow(2, 200) < float("inf"))
>>> True

