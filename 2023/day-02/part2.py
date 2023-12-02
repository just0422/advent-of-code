import sys
from collections import defaultdict

def power_set(color_counts):
    power = 1
    for count in color_counts.values():
        power *= count
    return power


with open(sys.argv[1]) as game:
    power_sum = 0
    while (line := game.readline().rstrip()):
        game_number = int(line.split(":")[0].split(" ")[1])

        sets = line.split(":")[1].split(";")
        color_counts = defaultdict(int)

        for color_set in sets:
            colors = color_set.split(",")

            for color_count in colors:
                count, color = color_count.strip().split(" ")
                color_counts[color] = max(int(count), color_counts[color])

        power_sum += power_set(color_counts)
    print(power_sum)
