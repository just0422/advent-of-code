import sys

with open(sys.argv[1]) as calibration:
    calibration_sum = 0
    while (line := calibration.readline().rstrip()):

        x = 0
        while not line[x].isnumeric():
            x += 1

        y = -1
        while not line[y].isnumeric():
            y -= 1

        calibration_sum += int(line[x] + line[y])

    print(calibration_sum)
