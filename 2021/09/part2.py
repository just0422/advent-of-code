import math
from collections import defaultdict

with open("input.txt") as all_points:
    points_map = []

    while (line := all_points.readline().rstrip()):
        points_line = []
        for point in list(line):
            points_line.append(int(point))

        points_map.append(points_line)

    def basin(i, j):
        if i < 0 or i == len(points_map):
            return 0
        if j < 0 or j == len(points_map[i]):
            return 0
        if points_map[i][j] < 0:
            return 0
        if points_map[i][j] == 9:
            return 0

        points_map[i][j] = -1

        north = basin(i - 1, j)
        west = basin(i, j - 1)
        south = basin(i + 1, j)
        east = basin(i, j + 1)

        return 1 + north + west + south + east

    basins = []
    for i in range(len(points_map)):
        for j in range(len(points_map[i])):
            result = basin(i, j)
            if result > 0:
                basins.append(result)

    basins.sort()
    basins.reverse()
    print(math.prod(basins[0:3]))
