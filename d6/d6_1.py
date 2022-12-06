f = open("d6_1.txt", "r")
lines = f.readlines()
input = lines[0]

for i in range(len(input)):
    if len(set(input[i:i+4])) == 4:
        print(i + 4)
        break