
f = open("d6_1.txt", "r")

lines = f.readlines()

input = lines[0]

# print(input[0:0+4])

for i in range(len(input)):
    if len(set(input[i:i+14])) == 14:
        print(i + 14)
        break