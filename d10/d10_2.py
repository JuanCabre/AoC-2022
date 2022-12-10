f = open("input.txt","r")
lines = [line.split("\n")[0] for line in f.readlines()]

x = 1
cycle = 0
draw = ""
for line in lines:
    line = line.split()
    if abs(cycle - x) > 1:
        draw += "."
    else:
        draw += "#"

    if line[0] == "noop":
        cycle = (cycle + 1) % 40
        continue
    else:
        cycle = (cycle + 1) % 40
        if abs(cycle - x) > 1:
            draw += "."
        else:
            draw += "#"

        x += int(line[1])
        cycle = (cycle + 1) % 40

for i in range(0,len(draw),40):
    print(draw[i:i+40])