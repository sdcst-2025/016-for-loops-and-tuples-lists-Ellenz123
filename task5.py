#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
import math
nums = (5,-2,12,-8,14,16)

for i in nums:
    if i>0:
        x=math.sqrt(i)
        print(f"The square root of {i} is {x}")