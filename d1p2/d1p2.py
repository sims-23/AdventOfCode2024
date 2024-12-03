from collections import Counter

locations_1 = []
locations_2 = []

with open("./d1p2/input.txt", "rt") as file:
    for line in file:
        locations = line.split()
        locations_1.append(int(locations[0]))
        locations_2.append(int(locations[1]))

counts_loc = Counter(locations_2)

sim_count = 0
for loc in locations_1:
    if loc in counts_loc:
        sim_count += loc * counts_loc[loc]

print(sim_count)


