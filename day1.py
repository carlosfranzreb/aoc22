calories_per_elf = [0]
with open("day1.txt") as f:
    for line in f:
        if line == "\n":
            calories_per_elf.append(0)
        else:
            calories_per_elf[-1] += int(line)

print(max(calories_per_elf))

max_3 = list()
while len(max_3) < 3:
    max_value = max(calories_per_elf)
    try:
        max_3.append(calories_per_elf.pop(calories_per_elf.index(max_value)))
    except ValueError:
        continue
print(max_3, sum(max_3[:3]))
