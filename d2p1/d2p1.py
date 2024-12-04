num_of_safe = 0

def is_safe_increasing(report: list[int]) -> int: 
    for i in range(len(report)-1):
        if int(report[i+1]) in range(int(report[i])+1, int(report[i])+4):
            continue
        else:
            return 0
    return 1

def is_safe_decreasing(report: list[int]) -> int: 
    for i in range(len(report)-1):
        if int(report[i+1]) in range(int(report[i])-3, int(report[i])):
            continue
        else:
            return 0
    return 1

def is_safe(report: list[int]) -> int:
    return is_safe_increasing(report) + is_safe_decreasing(report)

with open("./d2p1/input.txt", "rt") as file:
    for line in file:
        report = line.split()
        num_of_safe += is_safe(report)

print(num_of_safe)