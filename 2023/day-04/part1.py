import sys
import math

with open(sys.argv[1]) as cards:
    points = 0
    while (line := cards.readline().rstrip()):
        game = line.split(':')[1].split("|")

        winning = [int(num) for num in game[0].split(" ") if num.isnumeric()]
        have = [int(num) for num in game[1].split(" ") if num.isnumeric()]

        intersection = list(set(winning) & set(have))

        if len(intersection) == 0:
            continue

        points += int(math.pow(2, len(intersection) - 1))
    print(points)
