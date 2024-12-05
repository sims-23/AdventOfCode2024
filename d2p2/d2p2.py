num_of_safe = 0

#dampener allows for one single bad level
def is_safe_increasing(report: list[str]) -> int: 
    bad_level = False
    i = 0
    while i<len(report)-1:
        if int(report[i+1]) in range(int(report[i])+1, int(report[i])+4):
            i=i+1
            continue
        if bad_level:
            return 0
        if i == len(report) - 2:
            return 1
        if i + 2 < len(report) and int(report[i+2]) in range(int(report[i])+1, int(report[i])+4):
            bad_level = True
            i += 2
            continue
        if i == 0 and i + 2 < len(report) and int(report[i+2]) in range(int(report[i+1])+1, int(report[i+1])+4):
            bad_level = True
            i += 1
            continue
        return 0
    return 1

def is_safe_decreasing(report: list[str]) -> int: 

    bad_level = False
    i = 0
    while i<len(report)-1:
        if int(report[i+1]) in range(int(report[i])-3, int(report[i])):
            i=i+1
            continue
        if bad_level:
            return 0
        if i == len(report) - 2:
            return 1
        if i + 2 < len(report) and int(report[i+2]) in range(int(report[i])-3, int(report[i])):
            bad_level = True
            i += 2
            continue
        if i == 0 and i + 2 < len(report) and int(report[i+2]) in range(int(report[i+1])-3, int(report[i+1])):
            bad_level = True
            i += 1
            continue
        return 0
    return 1

def is_safe(report: list[int]) -> int:
    return is_safe_increasing(report) + is_safe_decreasing(report)

with open("./d2p2/input.txt", "rt") as file:
    for line in file:
        report = line.split()
        num_of_safe += is_safe(report)

print(num_of_safe)