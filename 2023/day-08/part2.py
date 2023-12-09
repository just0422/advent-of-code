import sys
from collections import defaultdict

# directions = list("RL")
directions = list("LRRLRRRLRRLRRLRRRLRRLRLLRRRLRRRLRRRLRRRLRRRLRRLLRRRLLRLRRRLRRLRRRLLRRRLRLLRRLRLLRLRLLRRLRRRLRRLLRRRLRRRLRLRRRLRRRLRRRLRRRLRLRRRLLRRRLRRLRRRLRLRRRLRRLRLLLLLRRRLRRRLRRRLRRRLRRLLRLRLRRLRRLLRRRLRRRLRRRLLLRRRLRRRLRRRLRLRRRLLRLRLRRLRRLRRRLRRLRRRLRRRLRRRLRRLLRRRLRRLRRLRLLRRRR")

class Node:
    def __init__(self, source, left, right):
        self.source = source
        self.left = left
        self.right = right

    def move(self, direction):
        if direction == "R":
            return self.right

        if direction == "L":
            return self.left

    def __str__(self):
        return f"{self.source} - ({self.left}, {self.right})"
    def __repr__(self):
        return str(self)

def all_finished(sources):
    for source in sources:
        if source[2] != "Z":
            return False
    return True

def any_finished(sources):
    for source in sources:
        if source[2] == "Z":
            return True
    return False

network = {}
with open(sys.argv[1]) as network_file:
    while (mapping := network_file.readline().rstrip()):
        source = mapping.split(" = ")[0]
        left, right = mapping.split(" = ")[1].split(", ")

        left = left[1:]
        right = right[0:3]

        network[source] = Node(source, left, right)

    current = [source for source in network.keys() if source[2] == "A"]
    print(current)

    direction_index = 0
    steps = 0
    while not all_finished(current):
        direction = directions[direction_index]

        temp_current = []
        for source in current:
            node = network[source]
            temp_current.append(node.move(direction))

        current = temp_current

        steps += 1
        direction_index += 1
        direction_index %= len(directions)

    print(steps)

    # I did the following by hand, but it oculd probably write the code :)
    # TODO: Find the out how long each step took, find the LCM
