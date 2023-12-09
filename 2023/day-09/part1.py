import sys
from collections import defaultdict

def check_zeros(seq):
    for num in seq:
        if num != 0:
            return False
    return True

def difference_down(seq):
    if check_zeros(seq):
        return 0

    next_diff = difference_down([seq[x] - seq[x-1] for x in range(1, len(seq))])

    return seq[len(seq) - 1] + next_diff

with open(sys.argv[1]) as sequence_file:
    sequence_sum = 0
    while (line := sequence_file.readline().rstrip()):
        sequence = [int(x) for x in line.split(' ')]

        sequence_sum += difference_down(sequence)

    print(sequence_sum)
