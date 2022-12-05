import queue

crates = [["Z","P","M","H","R"],
    ["P","C","J","B"],
    ["S","N","H","G","L","C","D"],
    ["F","T","M","D","Q","S","R","L"],
    ["F","S","P","Q","B","T","Z","M"],
    ["T","F","S","Z","B","G"],
    ["N","R","V"],
    ["P","G","L","T","D","V","C","M"],
    ["W","Q","N","J","F","M","L"]]

queues = []
for c in crates:
    q = queue.LifoQueue()
    for b in c:
        q.put(b)
    queues.append(q)


f = open("d5_1.txt","r")
lines = f.readlines()

for line in lines:
    input = [int(s) for s in line.split() if s.isdigit()]
    amount = input[0]
    position = input[1] - 1
    destination = input[2] - 1

    items = []
    for i in range(amount):
        items.append(queues[position].get())

    for i in reversed(items):
        queues[destination].put(i)

for q in queues:
    print(q.get())