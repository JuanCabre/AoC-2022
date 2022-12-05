from collections import Counter
import string

f = open("d3_1.txt","r")

lines = f.readlines()
for l in range(len(lines)):
    lines[l] = lines[l].split('\n')[0]

repeated = []
for l in range(0,len(lines),3):
    c1 = lines[l]
    c2 = lines[l + 1]
    c3 = lines[l + 2]

    found_all = False
    for i in c1:
        if found_all:
            break
        found_2 = False
        for j in c2:
            if found_2:
                break
            if i == j:
                found_2 = True
                for k in c3:
                    if i == k:
                        repeated.append(i)
                        found_all = True
                        break
# print(repeated)

# find the score
score = 0
points = list(string.ascii_letters)
for letter in repeated:
    for i in range(len(points)):
        if letter == points[i]:
            score += i + 1

print(score)