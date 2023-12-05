import sys
from collections import defaultdict

processed = []
def is_near_symbol(grid, x, y):
    x_coords = list(range(x - 1, x + 2))
    y_coords = list(range(y - 1, y + 2))

    if grid[x][y] == '.':
        return False

    if (x, y) in processed:
        return False

    for x1 in x_coords:
        for y1 in y_coords:
            if x1 == x and y1 == y:
                continue

            if x1 < 0 or y1 < 0:
                continue

            if x1 >= len(grid) or y1 >= len(grid[x]):
                continue

            if not grid[x1][y1].isalnum() and not grid[x1][y1] == '.':
                return True
    return False

def find_number(grid, x, y):
    left_side = y
    while left_side >= 0 and grid[x][left_side].isnumeric():
        left_side -= 1

    right_side = y
    while right_side < len(grid[x]) and grid[x][right_side].isnumeric():
        right_side += 1

    return int(''.join(grid[x][left_side + 1: right_side])), left_side + 1, right_side



with open(sys.argv[1]) as grid_file:
    game_sum = 0
    grid = []
    while (line := grid_file.readline().rstrip()):
        grid.append(list(line))


    numbers = []
    processed = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if (x,y) in processed:
                continue
            if is_near_symbol(grid, x, y):
                number, low, high = find_number(grid, x, y)

                for y_c in range(low, high):
                    processed.append((x, y_c))

                numbers.append(number)

    print(sum(numbers))
