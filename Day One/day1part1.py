from array import *
import re

# Read the file in line by line 

calibration = open('day1.txt', 'r')
lines = calibration.readlines()

res = []

for line in lines: 
    # Find the first and last numeric digit in each line
    match = re.findall(r'\d', line)
    first = match[0][0]
    last = match[-1]

    # Combine those two numbers to find the value (ex: 3 + 8 = 38)
    res.append(first + last)

    # Convert the values to integers
    res = list(map(int, res))

# Sum the values from each line together to get the total 
total = sum(res)
print(total)
