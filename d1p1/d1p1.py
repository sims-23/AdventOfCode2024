locations_1 = []
locations_2 = []

# Personal note: with statement creates a context manager (generally this handles setup and clean up for an operation - a smart wrapper (wrapper)). 
# In this case automatically handles closing file when you're done with it. 
# REMINDER: Look over software design patterns and uses
# open() - built in python fn 

with open("./d1p1/input.txt", "rt") as file:
    for line in file:
        locations = line.split()
        locations_1.append(int(locations[0]))
        locations_2.append(int(locations[1]))

locations_1.sort()
locations_2.sort()

#assuming lengths are the same, but putting a check in just in case  although instructions weren't given instructions to do in that case
if len(locations_1) != len(locations_2):
    print("lengths aren't the same")

distance = 0
for i in range(len(locations_1)):
    distance += abs(locations_1[i]-locations_2[i])

print(distance)

