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
            score += X
        case "Y":
            score += Y
        case "Z":
            score += Z

    if s[0] == "A":
        match s[1]:
            case "X":
                score += draw
            case "Y":
                score += win
            case "Z":
                score += loss

    elif s[0] == "B":
        match s[1]:
            case "X":
                score += loss
            case "Y":
                score += draw
            case "Z":
                score += win

    elif s[0] == "C":
        match s[1]:
            case "X":
                score += win
            case "Y":
                score += loss
            case "Z":
                score += draw

    results.append(score)

print(np.sum(results))