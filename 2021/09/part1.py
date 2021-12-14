def compare(points_map, i, j, i2, j2):
    try:
        if i2 < 0 or j2 < 0:
            return True
        return points_map[i][j] < points_map[i2][j2]
    except:
        return True

with open("input.txt") as all_points:
    points_map = []

    while (line := all_points.readline().rstrip()):
        points_line = []
        for point in list(line):
            points_line.append(int(point))

        points_map.append(points_line)

    low_points = []
    for i in range(len(points_map)):
        for j in range(len(points_map[i])):
            north = compare(points_map, i, j, i-1, j)
            south = compare(points_map, i, j, i+1, j)
            east = compare(points_map, i, j, i, j-1)
            west = compare(points_map, i, j, i, j+1)

            if j in [44,45,46] and i == 0:
                print(points_map[i][j], north, south, east, west)

            if north and south and east and west:
                low_points.append(points_map[i][j])

    print(sum([x + 1 for x in low_points]))
