with open("input.txt") as octopi:
    grid = []
    grid_flashes = []
    while (line := octopi.readline().rstrip()):
         octos = [int(x) for x in list(line)]
         grid_flash = [False for _ in list(line)]
         grid.append(octos)
         grid_flashes.append(grid_flash)

    def reset_flashes():
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid_flashes[i][j] = False

    flashes = 0
    def flash(i, j):
        global flashes
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return
        if grid_flashes[i][j]:
            return
        if grid[i][j] >= 9:
            grid_flashes[i][j] = True
            flashes += 1
            grid[i][j] = 0

            for mi in [i-1, i, i+1]:
                for mj in [j-1, j, j+1]:
                    flash(mi, mj)
        else:
            grid[i][j] += 1

    def nirvana():
        return sum([sum(x) for x in grid]) == 0

    x = 0
    while not nirvana():
        x += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                flash(i, j)

        reset_flashes()

    print(x)
    print(flashes)
