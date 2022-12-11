import queue


class Monkey:
    def __init__(self, items, test, operation):
        self.items = queue.Queue()
        self.test = test
        self.operation = operation
        self.targets = []
        self.inspected = 0
        for i in items:
            self.items.put(i)

    def setTargets(self, targets):
        self.targets = targets

    def takeItem(self, item):
        self.items.put(item)

    def makeTurn(self):
        while not self.items.empty():
            self.inspected += 1
            i = self.items.get()
            # Maaaaaaanoooo. Es el mcm!!!!!!!! Es aritmetica modular!!!
            # Todas las operaciones que se le hacen al numero dan igual. Solo
            # importa que los tests manden los resultados a los monos correctos.
            # Si tomamos el residuo de la division por el mcm del test de los
            # monos "dañamos" el numero pero preservamos la propiedad de tests
            # correctos que es lo que importa>
            new = self.operation(i) % 9699690
            if new % self.test == 0:
                self.targets[0].takeItem(new)
            else:
                self.targets[1].takeItem(new)

monkeys = []
def op0(old):
    return old * 19
monkeys.append(Monkey([59, 74, 65, 86], 7, op0))

def op1(old):
    return old + 1
monkeys.append(Monkey([62, 84, 72, 91, 68, 78, 51], 2, op1))

def op2(old):
    return old + 8
monkeys.append(Monkey([78, 84, 96], 19, op2))

def op3(old):
    return old * old
monkeys.append(Monkey([97, 86], 3, op3))

def op4(old):
    return old +6
monkeys.append(Monkey([50], 13, op4))

def op5(old):
    return old * 17
monkeys.append(Monkey([73, 65, 69, 65, 51], 11, op5))

def op6(old):
    return old + 5
monkeys.append(Monkey([69, 82, 97, 93, 82, 84, 58, 63], 5, op6))

def op7(old):
    return old + 3
monkeys.append(Monkey([81, 78, 82, 76, 79, 80], 17, op7))

monkeys[0].setTargets([monkeys[6],monkeys[2]])
monkeys[1].setTargets([monkeys[2],monkeys[0]])
monkeys[2].setTargets([monkeys[6],monkeys[5]])
monkeys[3].setTargets([monkeys[1],monkeys[0]])
monkeys[4].setTargets([monkeys[3],monkeys[1]])
monkeys[5].setTargets([monkeys[4],monkeys[7]])
monkeys[6].setTargets([monkeys[5],monkeys[7]])
monkeys[7].setTargets([monkeys[3],monkeys[4]])

for round in range(10000):
    for monkey in monkeys:
        monkey.makeTurn()

inspectedCounts = []
for monkey in monkeys:
    inspectedCounts.append(monkey.inspected)
    print(monkey.inspected)

inspectedCounts.sort(reverse=True)
print(inspectedCounts[0]*inspectedCounts[1])