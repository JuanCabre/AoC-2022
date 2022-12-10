f = open("input.txt","r")
lines = [line.split("\n")[0] for line in f.readlines()]

powers = []
marks = [20, 60, 100, 140, 180, 220]
i = 0
x = 1
cycle = 1
for line in lines:
    line = line.split()

    if i <= len(marks) -1 and cycle >= marks[i]:
        powers.append(x * marks[i])
        i+=1

    if line[0] == "noop":
        cycle +=1
        continue
    else:
        cycle += 1
        if i <= len(marks) -1 and cycle >= marks[i]:
            powers.append(x * marks[i])
            i+=1
        cycle += 1
        x += int(line[1])

print(powers)
print(sum(powers))