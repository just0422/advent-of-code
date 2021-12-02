with open("input.txt") as commands:
    horizontal = 0
    depth = 0
    aim = 0
    while (line := commands.readline().rstrip()):
        direction, distance = line.split(' ')
        distance = int(distance)

        if direction == "forward":
            horizontal += distance
            depth += aim * distance

        if direction == "up":
            aim -= distance

        if direction == "down":
            aim += distance

        if depth < 0:
            print("scream")

    print(horizontal)
    print(depth)
    print(aim)
    print(horizontal * depth)
