import numpy as np

f = open("input.txt","r")
lines = f.readlines()
for l in range(len(lines)):
    lines[l] = lines[l].split('\n')[0]

input = []
for line in lines:
    numbers = [int(n) for n in line]
    input.append(numbers)

input = np.array(input, np.int32)
rowCount, columnCount = input.shape

def isHigher(serie, h):
    for s in serie:
        if s >= h:
            return False
    return True

visibleTrees = 0
# Iterate over each tree
for y in range(rowCount):
    for x in range(columnCount):
        # If it's on the edge, it's vissible
        if x == 0 or y == 0 or x == columnCount -1 or y == rowCount -1:
            visibleTrees +=1
            continue

        h = input[y,x]
        # Go right
        if isHigher(input[y,x+1:],h):
            visibleTrees+=1
            continue
        # Go left
        if isHigher(input[y,:x],h):
            visibleTrees+=1
            continue
        # Go bottom
        if isHigher(input[y+1:,x],h):
            visibleTrees+=1
            continue
        # Go top
        if isHigher(input[:y,x],h):
            visibleTrees+=1
            continue

print(visibleTrees)
