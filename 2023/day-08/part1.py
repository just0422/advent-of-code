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

network = {}
with open(sys.argv[1]) as network_file:
    while (mapping := network_file.readline().rstrip()):
        source = mapping.split(" = ")[0]
        left, right = mapping.split(" = ")[1].split(", ")

        left = left[1:]
        right = right[0:3]

        network[source] = Node(source, left, right)

    current = "AAA"

    direction_index = 0
    steps = 0
    while current != "ZZZ":
        direction = directions[direction_index]

        node = network[current]

        current = node.move(direction)

        steps += 1
        direction_index += 1
        direction_index %= len(directions)

    print(steps)
