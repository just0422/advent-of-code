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

debug = False

active_action = False
node_to_split = None
def reduce(node, depth, left_right_values):
    global active_action
    global node_to_split
    if debug:
        print(f"///////// ENTER {str(node)=} {depth=} {left_right_values=})")
    if isinstance(node, Leaf):
        """
        if not active_action and node.check_split():
            active_action = True
            if node.parent.left == node:
                node.parent.left = node.split(node.parent)
                print("Split", node, node.parent.left)
            else:
                node.parent.right = node.split(node.parent)
                print("Split", node, node.parent.right)
            return True
        """
        if not node_to_split and node.check_split():
            node_to_split = node
            print(f"Found node to split - {node_to_split}")
        return node


    if debug:
        print("+++++ CALL - REDUCE LEFT")
    left_node = reduce(node.left, depth + 1, left_right_values)
    if left_node == True:
        if debug:
            print("+++++ RETURN - REDUCE LEFT ------ True")
        return True

    if debug:
        print("+++++ RETURN - REDUCE LEFT")

        print(f" --A-- {str(node)=} {str(left_right_values)=}")
        print("##### CALL - REDUCE RIGHT")
    right_node = reduce(node.right, depth + 1, left_right_values)
    if right_node == True:
        if debug:
            print("+++++ RETURN - REDUCE RIGHT ------ True")
        return True
    if debug:
        print("##### RETURN - REDUCE RIGHT")
        print(f" --B-- {right_node=}")

    # print(f"102 {node=} {left_right_values=} {isinstance(node.left , Leaf)=}")
    left_node_true = isinstance(left_node, Leaf)
    right_node_true = isinstance(right_node, Leaf)
    if debug:
        print(f"--C-- {left_node_true} {right_node_true} {depth=} {active_action=}")

    if not active_action:
        if left_node_true and right_node_true and depth >= 4:
            print(f"Exploding {node}")
            active_action = True
            left, right = node.explode()

            if debug:
                print(f"--D-- {str(node)=} {left.value=}")
                print(node.parent)
                print(f"--E-- {node.parent.left}")
            add_left(node, left.value)
            if debug:
                print(f"--F-- {str(node)=} {right.value=}")
            add_right(node, right.value)

            if node.parent.left == node:
                node.parent.left = Leaf(0, parent=node.parent)
            else:
                node.parent.right = Leaf(0, parent=node.parent)
            # node = Leaf(0)

            if debug:
                print("--H--", node.parent.left, node.parent.right)
                print("--H--", node.parent.left.parent, node.parent.right.parent)
            return True
        """
        if left_node_true and node.left.check_split():
            active_action = True
            print("Split", node.left)
            node.left = node.left.split(node)
            return True
        if right_node_true and node.right.check_split():
            active_action = True
            print("Split", node.right)
            node.right = node.right.split(node)
            return True
        """
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
    if debug:
        print("--G--", current_node, current_parent)
    while current_parent.right == current_node:
        current_node = current_parent
        current_parent = current_parent.parent

        if debug:
            print("--GG--", current_node, current_parent)
        if current_parent == None:
            return

    current_node = current_parent.right
    while not isinstance(current_node, Leaf):
        current_node = current_node.left

    current_node.value += value

    # Check if an explosion was returned
"""
tree = [[[[[9,8], 1], 2], 3], 4]
tree = [7,[6,[5,[4,[3,2]]]]]
tree = [[6,[5,[4,[3,2]]]],1]
tree = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
tree = [[[[4,3],4],4],[7,[[8,4],9]]]
addons = [[1,1]]

tree = [1,1]
addons = [[2,2], [3,3], [4,4], [5,5], [6,6]]

tree = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]

addons = [
    [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
    [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
    [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
    [7,[5,[[3,8],[1,4]]]],
    [[2,[2,2]],[8,[8,1]]],
    [2,9],
    [1,[[[9,3],9],[[9,0],[0,7]]]],
    [[[5,[7,4]],7],1],
    [[[[4,2],2],6],[8,7]]
]

tree = [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
addons = [
    [[[5,[2,8]],4],[5,[[9,9],0]]],
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
    [[[[5,4],[7,7]],8],[[8,3],8]],
    [[9,3],[[9,9],[6,[4,9]]]],
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
]
print(build_tree(tree))
root = build_tree(tree)
"""
with open("input.txt") as assignment:
    root_tree = ast.literal_eval(assignment.readline().rstrip())
    root = build_tree(root_tree)

    while (next_line := assignment.readline().rstrip()):
        new_tree = ast.literal_eval(next_line)
        root = Node(left=root, right=build_tree(new_tree))
        root.left.parent = root
        root.right.parent = root
        print(root)
        active_action = True
        while active_action:

            print("===="*20)
            active_action = False
            node_to_split = None
            if not reduce(root, 0, None) and node_to_split:
                active_action = True
                if node_to_split.parent.left == node_to_split:
                    node_to_split.parent.left = node_to_split.split(node_to_split.parent)
                    print("Split", node_to_split, node_to_split.parent.left)
                else:
                    node_to_split.parent.right = node_to_split.split(node_to_split.parent)
                    print("Split", node_to_split, node_to_split.parent.right)
            print(root)
        print("---", root)

print(root)

"""
after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
"""

def in_order_traversal(node):
    if isinstance(node, Leaf):
        return node.value


    left = in_order_traversal(node.left)
    right = in_order_traversal(node.right)

    return 3 * left + 2 * right

print(in_order_traversal(root))
