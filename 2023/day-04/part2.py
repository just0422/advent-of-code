import sys
import math
from collections import defaultdict

with open(sys.argv[1]) as cards:
    points = 0
    win_counts = defaultdict(int)
    win_values = defaultdict(int)
    while (line := cards.readline().rstrip()):
        game_number = int(line.split(":")[0].split(" ")[-1])
        game = line.split(':')[1].split("|")

        winning = [int(num) for num in game[0].split(" ") if num.isnumeric()]
        have = [int(num) for num in game[1].split(" ") if num.isnumeric()]

        intersection = list(set(winning) & set(have))

        win_counts[game_number] += 1
        if len(intersection) == 0:
            continue

        for x in range(game_number + 1, game_number + len(intersection) + 1):
            win_counts[x] += win_counts[game_number]

        win_values[game_number] = math.pow(2, len(intersection) - 1)

    print(sum(win_counts.values()))
