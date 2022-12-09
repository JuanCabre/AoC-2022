import numpy as np
f = open("input.txt","r")
lines = [line.split("\n")[0] for line in f.readlines()]

def moveTail(head,tail):
    x,y = 0,1
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

x,y = 0,1
positions = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
visited = {tuple(positions[-1])}
for line in lines:
    direction = line.split()[0]
    steps = int(line.split()[1])
    head = positions[0]

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

        for i in range(len(positions) -1):
            moveTail(positions[i],positions[i+1])

        visited.add(tuple(positions[-1]))

print(len(visited))