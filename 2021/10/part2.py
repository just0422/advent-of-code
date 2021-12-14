from collections import defaultdict
from statistics import median


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    def peek(self):
        if len(self.stack) == 0:
            return -1
        return ord(self.stack[-1])
    def pop(self):
        return self.stack.pop()
    def empty(self):
        return len(self.stack) == 0

bad_chars = defaultdict(int)
char_map = {"(":1, "[":2, "{":3, "<":4}
line_scores = []
with open("input.txt") as lines:
    while (line := lines.readline().rstrip()):
        stack = Stack()
        good_line = True
        for char in list(line):
            if char in "([{<":
                stack.push(char)
            else:
                value = stack.peek()
                if value == -1:
                    bad_chars[char] += 1
                    good_line = False
                    break

                ichar = ord(char)
                if ichar - value not in [1,2]:
                    bad_chars[char] += 1
                    good_line = False
                    break
                stack.pop()
        if good_line:
            line_score = 0
            while not stack.empty():
                line_score *= 5
                line_score += char_map[stack.pop()]
            line_scores.append(line_score)


print(line_scores)
print(median(line_scores))
