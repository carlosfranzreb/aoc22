import string


priorities = string.ascii_lowercase + string.ascii_uppercase

"""
Q1: find the item type that appears in both compartments of each rucksack. What is
the sum of the priorities of those item types?
"""

out = 0
with open("day3.txt") as f:
    for line in f:
        line = line.strip()
        split = len(line) // 2
        first, second = line[:split], line[split:]
        for item in first:
            if item in second:
                out += priorities.index(item) + 1
                break
print(out)

"""
Q2: find the item type that corresponds to the badges of each three-Elf group. What is
the sum of the priorities of those item types?
"""

out = 0
group = list()
with open("day3.txt") as f:
    for line in f:
        group.append(line.strip())
        if len(group) == 3:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    out += priorities.index(item) + 1
                    break
            group = list()
print(out)
