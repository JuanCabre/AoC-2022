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

def scoreCalculator(serie, h):
    visibles = 0
    for s in serie:
        visibles += 1
        if s >= h:
            break
    return visibles

scores = []
# Iterate over each tree
for y in range(rowCount):
    for x in range(columnCount):
        score = 1

        h = input[y,x]
        # Go right
        score *= scoreCalculator(input[y,x+1:],h)
        # Go left
        score *= scoreCalculator(np.flipud(input[y,:x]),h)
        # Go bottom
        score *= scoreCalculator(input[y+1:,x],h)
        # Go top
        score *= scoreCalculator(np.flipud(input[:y,x]),h)

        scores.append(score)

print(np.max(scores))
