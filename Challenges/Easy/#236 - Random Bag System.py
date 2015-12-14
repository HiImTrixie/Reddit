import random


def first(n):
    bag = []
    z = {0: "O", 1: "I", 2: "S", 3: "Z", 4: "L", 5: "J", 6: "T"}
    while n > len(bag):
        x = random.randint(0, 6)
        if len(z) != 0:
            if x not in z:
                pass
            else:
                bag.append(z.pop(x))
        else:
            z = {0: "O", 1: "I", 2: "S", 3: "Z", 4: "L", 5: "J", 6: "T"}
    return bag


def second():
    pieces = ["O", "I", "S", "Z", "L", "J", "T"]
    string = ""
    for i in range(7):
        random.shuffle(pieces)
        string += "".join(pieces)
    string += pieces[random.randint(0, 6)]
    return string
