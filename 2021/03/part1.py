with open("input.txt") as depths:
    zeros = None
    line_count = 0
    while (line := depths.readline().rstrip()):
        line_count += 1
        digits = list(line)

        if not zeros:
            zeros = [0] * len(digits)
        for i in range(len(digits)):
            if  digits[i] == '0':
                zeros[i] += 1

    ones = [ line_count - x for x in zeros ]
    print(ones)
    print(zeros)

    ones.reverse()
    zeros.reverse()

    digit = 1
    gamma = 0
    epsilon = 0
    for zero, one in zip(zeros, ones):
        if one > zero:
            gamma += digit
        else:
            epsilon += digit

        digit *= 2

    print(gamma, epsilon)
    print(gamma * epsilon)
