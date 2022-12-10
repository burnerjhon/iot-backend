# Dynamically typed
# multiple assignments
n, m = 0, "abc"
a , b,c = 0.34, "workin", False

# Increment
n = n+1 
n += 1 
#  n++ does not work

# None is null in python
n = None

# If statements
n = 1 
# indentation does to work instead of
# curly braces
if n > 2:
    n = 3
elif n == 2:
     n *= 2
else: 
    n = 2             
# multi line conditions 
# and and or are used
if ((n>2 and n!=m) or n==m):
    n=3
    
# Loops
# While
while n < 5:
    print(n)  
# For 
for i in range(5):
    print(i) 
    # prints till 5 with increment value of 1
for i in range(1,6):
    print(i)
    # prints from 1 to 5 excluding 6
for i in  range(1, 7, 5):
    print(i)
    # prints 1 and 7 with the increment of 5
    
# Division
# for decimal division
print(5/2)
# for rounded division
print(5//2)
# negative numbers will be rounded down to the least number
print(-3//2)
# to round negative numbers to higher number
print(int(-3/2))

# Modulus
print(10%3)
# negative mods again round down to the least value 
# rather than the highest one
# to be consistent use math module functions

# math helpers
import math
# modulus
print(math.fmod(-10,3))
# more math helpers
# round down 
print(math.floor(3/2))
# round down 
print(math.ceil(4/3))
# square root
print(math.sqrt(2))
# power
print(math.pow(2, 3))

# max int
float("inf")
# min int
float("-inf")

# Lists aka Arrays
arr = [1,2,3]
# to add a num to the last
arr.append(4)
# to remove the last num
arr.pop()
# to add in the start
arr.insert(1,7)

# Initialising an array of size n with the value of 1
arr = [1] * 5

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1])
>>> 3

# Indexing -2 is the second to last value, etc.
print(arr[-2])
>>> 2

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])
>>> [2, 3]

# Similar to for-loop ranges, last index is non-inclusive

print(arr[0:4])

>>> [1, 2, 3, 4]

# But no out of bounds error

print(arr[0:10])

>>> [1, 2, 3, 4]

# Unpacking

a, b, c = [1, 2, 3]

print(a, b, c)

>>> 1, 2, 3

# Be careful though, this throws an error

a, b = [1, 2, 3]

# Looping through arrays

nums = [1, 2, 3]

# Using index

for i in range(len(nums)):

    print(nums[i])

>>> 1 2 3

# Without index

for n in nums:

    print(n)

>>> 1 2 3

# With index and value

for i, n in enumerate(nums):

    print(i, n)

>>> 0 1

>>> 1 2

>>> 2 3

# Loop through multiple arrays simultaneously with unpacking

nums1 = [1, 3, 5]

nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):

    print(n1, n2)

>>> 1 2

>>> 3 4

>>> 5 6
