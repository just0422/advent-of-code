import sys

left = []
right = []

with open(sys.argv[1]) as points:
    for line in points:
        # Split the line into two numbers based on whitespace
        l, r = map(int, line.split())
        # Append the numbers to their respective lists
        left.append(l)
        right.append(r)

left_sorted = sorted(left)
right_sorted = sorted(right)

sums = 0

for l, r in zip(left_sorted, right_sorted):
    sums += abs(l - r)

print(sums)
