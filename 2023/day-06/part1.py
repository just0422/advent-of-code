import sys
import math

times = [46689866]
distances = [358105418071080]
# times = [71530]
# distances = [940200]

win_counts = []
for time, distance in zip(times, distances):
    winners = []
    for x in range(time):
        left_over = time - x
        dist = left_over * x

        if dist > distance:
            winners.append(x)

    win_counts.append(len(winners))

# print(win_counts)
answer = 1
for count in win_counts:
    answer *= count
print(answer)
