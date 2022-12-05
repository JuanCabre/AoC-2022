import numpy as np

A, X = 1, 1
B, Y = 2, 2
C, Z = 3, 3

loss, draw, win = 0, 3, 6

f = open("d2_1.txt", 'r')
lines = f.readlines()

results = []
for line in lines:
    score = 0
    line = line.replace('\n', '')
    s = line.split(" ")
    match s[1]:
        case "X":
            score += loss
        case "Y":
            score += draw
        case "Z":
            score += win

    if s[0] == "A":
        match s[1]:
            case "X":
                score += C
            case "Y":
                score += A
            case "Z":
                score += B

    elif s[0] == "B":
        match s[1]:
            case "X":
                score += A
            case "Y":
                score += B
            case "Z":
                score += C

    elif s[0] == "C":
        match s[1]:
            case "X":
                score += B
            case "Y":
                score += C
            case "Z":
                score += A

    results.append(score)

print(np.sum(results))