import queue

f = open("input.txt", "r")
lines = f.readlines()
for l in range(len(lines)):
    lines[l] = lines[l].split('\n')[0]


class Directory:

    def __init__(self, n):
        self.name = n
        self.subdirs = {}
        self.files = []
        self.parent = Directory
        self.sumOverTarget = 0

    def addSubdir(self, s):
        self.subdirs[s.name] = s

    def getSize(self):
        size = 0
        for f in self.files:
            size += f
        return size

    def getTotalSize(self):
        size = self.getSize()
        l = len(self.subdirs)
        if l == 0:
            return size
        for _, s in self.subdirs.items():
            size += s.getTotalSize()
        return size

rootDir = Directory("root")
currentDir = rootDir

for line in lines:
    line = line.split()

    if line[0] == "$":
        if line[1] == "ls":
            continue
        elif line[1] == "cd":
            if line[2] == "..":
                currentDir = currentDir.parent
            else:
                currentDir = currentDir.subdirs[line[2]]

    elif line[0] == "dir":
        # If it's dir. Add the directory to the tree
        newDir = Directory(line[1])
        newDir.parent = currentDir
        currentDir.subdirs[line[1]] = newDir

    elif line[0].isdigit():
        # If it's a file, add it to the directory
        currentDir.files.append(int(line[0]))


# Find the sum
currentDirs = []
for _, d in rootDir.subdirs.items():
    currentDirs.append(d)
complete = False
sizes = []
while not complete:
    tmpDirs = []
    for d in currentDirs:
        sizes.append(d.getTotalSize())
        for _, c in d.subdirs.items():
            tmpDirs.append(c)
    currentDirs = tmpDirs
    if len(currentDirs) == 0:
        complete = True

sizesUnderTarget = [s for s in sizes if s<=100000]
print(sum(sizesUnderTarget))