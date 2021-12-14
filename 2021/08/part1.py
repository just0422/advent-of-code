with open("test_input.txt") as numbers:
    unique_digits = 0
    while (line := numbers.readline().rstrip()):
        io = line.split(' | ')

        inp = io[0]
        out = io[1]

        digits = out.split(' ')
        for digit in digits:
            if len(digit) in [2,3,4,7]:
                unique_digits += 1

    print(unique_digits)
