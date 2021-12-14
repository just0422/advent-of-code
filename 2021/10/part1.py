from collections import defaultdict


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

stack = Stack()
bad_chars = defaultdict(int)
with open("input.txt") as lines:
    while (line := lines.readline().rstrip()):
        for char in list(line):
            if char in "([{<":
                stack.push(char)
            else:
                value = stack.peek()
                if value == -1:
                    bad_chars[char] += 1
                    break

                ichar = ord(char)
                if ichar - value not in [1,2]:
                    bad_chars[char] += 1
                    break
                stack.pop()

for k,v in bad_chars.items():
    print(k, v)

print(bad_chars[")"]* 3 + bad_chars["]"] *57 + bad_chars["}"] * 1197 + bad_chars[">"] * 25137)
