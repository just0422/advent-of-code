import sys

reports = []

muls = []

def result(eq):
    if eq[:3] != "mul":
        return 0

    if eq[3] != "(" or eq[len(eq) - 1] != ")":
        return 0

    # possible numbers idx: 4 - len(eq) - 2
    if eq[4].isdigit() and eq[5] == "," and eq[6: len(eq)- 1].isdigit():
        return int(eq[4]) * int(eq[6: len(eq) - 1])

    if eq[4:6].isdigit() and eq[6] == "," and eq[7: len(eq)- 1].isdigit():
        return int(eq[4:6]) * int(eq[7: len(eq) - 1])

    if eq[4:7].isdigit() and eq[7] == "," and eq[8: len(eq)- 1].isdigit():
        return int(eq[4:7]) * int(eq[8: len(eq) - 1])

    return 0


with open(sys.argv[1]) as report_file:
    line = report_file.readline()

total = 0
for x in range(len(line)):
    if line[x] == "m":
        for y in range(8, 13):
            total += result(line[x:x+y])

print(total)
