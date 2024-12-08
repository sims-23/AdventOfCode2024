import re
import math

with open("./d3p2/input.txt", "rt") as file:
    file_contents = file.read()

    total = 0

    vals = re.findall(r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', file_contents)

    enabled = True
    for val in vals:
        if val == 'do()':
            enabled = True
        elif val == 'don\'t()':
            enabled = False
        elif enabled:
            nums = re.findall(r'\d+', val)
            total += math.prod(map(int, nums))
        else:
            continue

print(total)

