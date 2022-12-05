import numpy as np

f = open("d1_1.txt",'r')
lines = f.readlines()

calories = []
c = 0
for line in lines:
    if line == '\n':
        calories.append(c)
        c = 0
        continue
    c += int(line.split('\n')[0])

print(max(calories))