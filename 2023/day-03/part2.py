import sys
from collections import defaultdict

def nearby_number_coordinates(grid, x, y):
    x_coords = list(range(x - 1, x + 2))
    y_coords = list(range(y - 1, y + 2))

    nearby_numbers = []
    for x1 in x_coords:
        for y1 in y_coords:
            if x1 == x and y1 == y:
                continue

            if x1 < 0 or y1 < 0:
                continue

            if x1 >= len(grid) or y1 >= len(grid[x]):
                continue

            if grid[x1][y1].isnumeric():
                nearby_numbers.append((x1, y1))
    return nearby_numbers

def find_number(grid, x, y):
    left_side = y
    while left_side >= 0 and grid[x][left_side].isnumeric():
        left_side -= 1

    right_side = y
    while right_side < len(grid[x]) and grid[x][right_side].isnumeric():
        right_side += 1

    number = ''.join(grid[x][left_side + 1: right_side])
    if len(number) == 0:
        return -1, -1, -1

    return number, left_side + 1, right_side



with open(sys.argv[1]) as grid_file:
    game_sum = 0
    grid = []
    while (line := grid_file.readline().rstrip()):
        grid.append(list(line))


    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != '*':
                continue

            number_coords = nearby_number_coordinates(grid, x, y)
            processed = []
            numbers = []

            for coord in number_coords:
                if coord in processed:
                    continue
                number, low, high = find_number(grid, coord[0], coord[1])

                if number == -1:
                    continue

                for y_c in range(low, high):
                    processed.append((coord[0], y_c))

                numbers.append(number)

            if len(numbers) == 2:
                game_sum += int(numbers[0]) * int(numbers[1])

    print(game_sum)
