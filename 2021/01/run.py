with open("input.txt") as depths:
    prev = -1
    increases = 0
    while (line := depths.readline().rstrip()):
        depth = int(line)
        if depth > prev:
            increases += 1

        prev = depth

    print(increases - 1)
