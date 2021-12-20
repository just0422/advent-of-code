import ast
import math
from collections import defaultdict


class Node():
    def __init__(self, parent = None, left=None, right=None):
        self.left = left
        self.right = right
        self.parent = parent

    def explode(self):
        return [self.left, self.right]

    def __str__(self):
        return f"[{self.left}, {self.right}]"

class Leaf():
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def check_split(self):
        return self.value >= 10

    def split(self, new_parent):
        left = math.floor(self.value / 2)
        right = math.ceil(self.value / 2)

        new_node = Node(left=Leaf(left), right=Leaf(right))
        new_node.left.parent = new_node
        new_node.right.parent = new_node
        new_node.parent = new_parent

        return new_node

    def __str__(self):
        return f"{self.value}"

def build_tree(tree):
    root = Node()

    left = tree[0]
    right = tree[1]

    root.left = Leaf(left) if isinstance(left, int) else build_tree(left)
    root.left.parent = root

    root.right = Leaf(right) if isinstance(right, int) else build_tree(right)
    root.right.parent = root

    return root

active_action = False
node_to_split = None
def reduce(node, depth, left_right_values):
    global active_action
    global node_to_split
    if isinstance(node, Leaf):
        if not node_to_split and node.check_split():
            node_to_split = node
        return node


    left_node = reduce(node.left, depth + 1, left_right_values)
    if left_node == True:
        return True

    right_node = reduce(node.right, depth + 1, left_right_values)
    if right_node == True:
        return True

    left_node_true = isinstance(left_node, Leaf)
    right_node_true = isinstance(right_node, Leaf)

    if not active_action and left_node_true and right_node_true and depth >= 4:
        active_action = True
        left, right = node.explode()

        add_left(node, left.value)
        add_right(node, right.value)

        if node.parent.left == node:
            node.parent.left = Leaf(0, parent=node.parent)
        else:
            node.parent.right = Leaf(0, parent=node.parent)

        return True
    return False

def add_left(node, value):
    current_node = node
    current_parent = node.parent
    while current_parent.left == current_node:
        current_node = current_parent
        current_parent = current_parent.parent

        if current_parent == None:
            return

    current_node = current_parent.left
    while not isinstance(current_node, Leaf):
        current_node = current_node.right

    current_node.value += value

def add_right(node, value):
    current_node = node
    current_parent = node.parent
    while current_parent.right == current_node:
        current_node = current_parent
        current_parent = current_parent.parent

        if current_parent == None:
            return

    current_node = current_parent.right
    while not isinstance(current_node, Leaf):
        current_node = current_node.left

    current_node.value += value

    # Check if an explosion was returned

def in_order_traversal(node):
    if isinstance(node, Leaf):
        return node.value


    left = in_order_traversal(node.left)
    right = in_order_traversal(node.right)

    return 3 * left + 2 * right

mags = []
with open("input.txt") as assignment:
    all_trees = []
    while (next_line := assignment.readline().rstrip()):
        all_trees.append(ast.literal_eval(next_line))

    for left_tree in all_trees:
        for right_tree in all_trees:
            if left_tree == right_tree:
                continue
            root = Node(left=build_tree(left_tree), right=build_tree(right_tree))
            root.left.parent = root
            root.right.parent = root

            active_action = True
            while active_action:

                active_action = False
                node_to_split = None
                if not reduce(root, 0, None) and node_to_split:
                    active_action = True
                    if node_to_split.parent.left == node_to_split:
                        node_to_split.parent.left = node_to_split.split(node_to_split.parent)
                    else:
                        node_to_split.parent.right = node_to_split.split(node_to_split.parent)
            mags.append( in_order_traversal(root))

# print(root)
print(max(mags))
