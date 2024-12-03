import sys

def report_is_safe(rep):
    for x in range(1, len(rep) - 1):
        left = rep[x-1]
        middle = rep[x]
        right = rep[x+1]

        if abs(left - middle) > 3 or abs(middle - right) > 3:
            return False

        if not (left < middle < right or left > middle > right):
            return False
    return True

reports = []

with open(sys.argv[1]) as report_file:
    for line in report_file:
        report = list(map(int, line.split()))
        reports.append(report)

unsafe_reports = []

for report in reports:
    if not report_is_safe(report):
        unsafe_reports.append(report)

safe_report_count = len(reports) - len(unsafe_reports)

print(safe_report_count)

for report in unsafe_reports:
    for x in range(len(report)):
        new_report = report[:x] + report[x + 1:]

        if report_is_safe(new_report):
            safe_report_count += 1
            break

print(safe_report_count)
