with open("input.txt") as depths:
    window = [-1, -1, -1]
    prev_sum = -1
    increases = 0
    while (line := depths.readline().rstrip()):
        del window[0]
        window.append(int(line))
        if -1 in window:
            continue

        if sum(window) > prev_sum:
            increases += 1

        prev_sum = sum(window)

    print(increases - 1)
