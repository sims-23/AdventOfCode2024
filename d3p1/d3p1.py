import re
import math

with open("./d3p1/input.txt", "rt") as file:
    file_contents = file.read()
    muls =re.findall(r'mul\(\d{1,3},\d{1,3}\)', file_contents)
    
    total = 0
    for mul in muls:
        nums = re.findall(r'\d+', mul)
        total += math.prod(map(int, nums))

print(total)