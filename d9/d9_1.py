import numpy as np
f = open("input.txt","r")
lines = [line.split("\n")[0] for line in f.readlines()]

x,y = 0,1
head = [0,0]
tail = [0,0]
visited = {tuple(tail)}
for line in lines:
    direction = line.split()[0]
    steps = int(line.split()[1])

    for i in range(steps):
        # Move head
        match direction:
            case "R":
                head[x] += 1
            case "L":
                head[x] -= 1
            case "U":
                head[y] += 1
            case "D":
                head[y] -= 1
        # Check position of tail
        dx = head[x] - tail[x]
        dy = head[y] - tail[y]
        if abs(dx) >= 2 or abs(dy) >= 2:
            # Tail must move
            if tail[y] == head[y]:
                tail[x] += 1 * np.sign(dx)
            elif tail[x] == head[x]:
                tail[y] += 1 * np.sign(dy)
            else:
                tail[y] += 1 * np.sign(dy)
                tail[x] += 1 * np.sign(dx)
            visited.add(tuple(tail))

print(len(visited))