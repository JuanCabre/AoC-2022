
f = open("d4_1.txt","r")

lines = f.readlines()
for l in range(len(lines)):
    lines[l] = lines[l].split('\n')[0]

total_overlaps = 0
runs = 0
l = 0
for line in lines:
    l+=1
    assignments = line.split(",")

    elf1_min = int(assignments[0].split("-")[0])
    elf1_max = int(assignments[0].split("-")[1])
    elf2_min = int(assignments[1].split("-")[0])
    elf2_max = int(assignments[1].split("-")[1])

    # Check if the first section overlaps with the second
    if (elf1_min >= elf2_min and elf1_min <= elf2_max) or (elf2_min >= elf1_min and elf2_min <= elf1_max):
        total_overlaps += 1
        print("first overlaps with seccond", elf1_min, elf1_max, elf2_min, elf2_max)

print(total_overlaps, l)