import sys
from collections import defaultdict

possible_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def valid_game(color_sum):
    for color in possible_cubes:
        if possible_cubes[color] < color_sum.get(color, 0):
            return False
    return True

with open(sys.argv[1]) as game:
    game_sum = 0
    while (line := game.readline().rstrip()):
        game_number = int(line.split(":")[0].split(" ")[1])

        sets = line.split(":")[1].split(";")
        color_sums = defaultdict(int)

        for color_set in sets:
            colors = color_set.split(",")

            for color_count in colors:
                count, color = color_count.strip().split(" ")
                color_sums[color] = max(int(count), color_sums[color])

        if valid_game(color_sums):
            game_sum += game_number
    print(game_sum)
