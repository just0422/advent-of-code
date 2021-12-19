import math
from collections import defaultdict

# with open("input.txt") as pairs:

class Node():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def explode(self):
        return [self.left, self.right]

    def __str__(self):
        return f"[{self.left}, {self.right}]"

class Leaf():
    def __init__(self, value):
        self.value = value

    def check_split(self):
        return self.value >= 10

    def split(self):
        left = math.floor(self.value / 2)
        right = math.ceil(self.value / 2)

        return Node(left=Leaf(left), right=Leaf(right))

    def __str__(self):
        return f"{self.value}"

def build_tree(tree):
    root = Node()

    left = tree[0]
    right = tree[1]

    root.left = Leaf(left) if isinstance(left, int) else build_tree(left)
    root.right = Leaf(right) if isinstance(right, int) else build_tree(right)

    return root


active_action = False
def reduce(node, depth, left_right_values):
    global active_action
    print(f"///////// ENTER {str(node)=} {depth=} {left_right_values=})")
    if isinstance(node, Leaf):
        if not active_action and node.check_split():
            active_action = True
            return node.split()
        return True

    if isinstance(left_right_values, list) and isinstance(left_right_values[1], Leaf) and isinstance(node.left, Leaf):
        print(f"Before Node - {str(node)=}")
        node.left.value += left_right_values[1].value
        print(f"After  Node - {str(node)=}")
        return [left_right_values[0], None]

    print("+++++ CALL - REDUCE LEFT")
    left_node = reduce(node.left, depth + 1, left_right_values)

    print("+++++ RETURN - REDUCE LEFT")
    print(f" 63 {node=} {left_node=}")
    if isinstance(left_node, Node):
        node.left = left_node
        return True
    left_right_values = left_node

    print(f" 69 {str(node)=} {str(left_node)=}")
    if isinstance(left_node, list) and None not in left_node:
        node.left = Leaf(0)

    print(f" 73 {str(node)=} {str(left_right_values)=} {isinstance(left_right_values, list)} {isinstance(node.right, Leaf)=}")
    if isinstance(left_right_values, list) and left_right_values[1] and isinstance(node.right, Leaf):
        node.right.value += left_right_values[1].value
        return [left_right_values[0], None]

    print(f" 80 {str(node)=} {str(left_right_values)=}")
    # If the left node gives me back a left node, that
    #  means I need to add it to the first left digit I find
    # BUt that won't be the case here, so I have to try else where
    # If I completely exit the function with a node, then set it to 0
    if isinstance(left_node, Leaf):
        return node.left_node

    print(f" 88 {str(node)=} {str(left_right_values)=}")
    print("##### CALL - REDUCE RIGHT")
    right_node = reduce(node.right, depth + 1, left_right_values)
    print("##### RETURN - REDUCE RIGHT")
    print(f" 88 {right_node=}")
    if isinstance(right_node, Node):
        node.right = right_node
        return True

    left_right_values = right_node
    if isinstance(right_node, list) and right_node[0]:
        if right_node[1]:
            node.right = Leaf(0)

        if isinstance(node.left, Leaf):
            node.left.value += left_right_values[0].value
            return [None, left_right_values[1]]


    print(f"102 {node=} {left_right_values=} {isinstance(node.left , Leaf)=}")
    left_node_true = isinstance(left_node, bool) and left_node
    right_node_true = isinstance(right_node, bool) and right_node
    print(f"105 {left_node_true} {right_node_true}")
    if left_node_true and right_node_true and depth >= 4 and not active_action:
        print(f"\t\t--- Exploding {node}")
        active_action = True
        return node.explode()

    return left_right_values

    # Check if an explosion was returned

tree = [[[[[9,8], 1], 2], 3], 4]
tree = [7,[6,[5,[4,[3,2]]]]]
tree = [[6,[5,[4,[3,2]]]],1]
tree = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
tree = [[[[4,3],4],4],[7,[[8,4],9]]]
tree = [1,1]
addons = [[2,2], [3,3], [4,4], [5,5], [6,6]]

tree = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
print(build_tree(tree))
root = build_tree(tree)

addons = [
    [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
]
"""
    [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
    [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
    [7,[5,[[3,8],[1,4]]]],
    [[2,[2,2]],[8,[8,1]]],
    [2,9],
    [1,[[[9,3],9],[[9,0],[0,7]]]],
    [[[5,[7,4]],7],1],
    [[[[4,2],2],6],[8,7]]
]
"""

for addon in addons:
    root = Node(left=root, right=build_tree(addon))
    print(root)
    active_action = True
    while active_action:

        print("===="*20)
        active_action = False
        reduce(root, 0, None)
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
        return [node.value]


    left = in_order_traversal(node.left)
    right = in_order_traversal(node.right)

    return left + right

print(in_order_traversal(root))
