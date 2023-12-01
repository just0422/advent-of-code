import sys

def check_number(number, string):
    num_str_len = len(number)
    if len(string) < num_str_len:
        return False

    return string[0:num_str_len] == number

def spells_digit(string):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for x in range(len(numbers)):
        if check_number(numbers[x], string):
            return x

    return None


with open(sys.argv[1]) as calibration:
    calibration_sum = 0
    while (line := calibration.readline().rstrip()):
        left_digit = 0

        for x in range(len(line)):
            if digit := spells_digit(line[x:]):
                left_digit = digit
                break
            if line[x].isnumeric():
                left_digit = int(line[x])
                break

        right_digit = 0
        for y in range(1, len(line) + 1):
            if digit := spells_digit(line[-y:]):
                right_digit = digit
                break
            if line[-y].isnumeric():
                right_digit = int(line[-y])
                break

        calibration_sum += left_digit * 10 + right_digit
    print(calibration_sum)
