from collections import Counter
import string

f = open("d3_1.txt","r")

lines = f.readlines()

repeated = []
for line in lines:
    # Split the strings in two halves
    l = len(line) - 1
    rs_1 = slice(0,l//2)
    rs_2 = slice(l//2, l)
    c1 = line[rs_1]
    c2 = line[rs_2]

    added = False
    for i in c1:
        if added:
            break
        for j in c2:
            if i == j:
                if not added:
                    repeated.append(i)
                    added = True

# find the score
score = 0
points = list(string.ascii_letters)
for letter in repeated:
    for i in range(len(points)):
        if letter == points[i]:
            score += i + 1

print(score)