import sys
from collections import defaultdict

left = []
right = []

with open(sys.argv[1]) as points:
    for line in points:
        # Split the line into two numbers based on whitespace
        l, r = map(int, line.split())
        # Append the numbers to their respective lists
        left.append(l)
        right.append(r)

counts = {}

left_counts = defaultdict(int)
right_counts = defaultdict(int)

for l in left:
    left_counts[l] += 1

for r in right:
    right_counts[r] += 1

total = 0
for l in left_counts:
    total += l * left_counts[l] * right_counts[l]

print(total)
