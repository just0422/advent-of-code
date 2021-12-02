with open("input.txt") as depths:
    horizontal = 0
    vertical = 0
    while (line := depths.readline().rstrip()):
        direction, distance = line.split(' ')
        distance = int(distance)

        if direction == "forward":
            horizontal += distance

        if direction == "up":
            vertical -= distance

        if direction == "down":
            vertical += distance

        if vertical < 0:
            print("scream")

    print(horizontal)
    print(vertical)
    print(horizontal * vertical)
