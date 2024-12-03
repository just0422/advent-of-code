import sys

reports = []

with open(sys.argv[1]) as report_file:
    for line in report_file:
        report = list(map(int, line.split()))
        reports.append(report)

unsafe = 0

for report in reports:
    for x in range(1, len(report) - 1):
        left = report[x-1]
        middle = report [x]
        right = report[x+1]

        if abs(left - middle) > 3 or abs(middle - right) > 3:
            unsafe += 1
            break

        if not (left < middle < right or left > middle > right):
            unsafe += 1
            break

print (len(reports), len(reports) - unsafe, unsafe)
