x1 = 119
x2 = 176

y1 = -84
y2 = -141

possible_ys = range(y2, abs(y2))
possible_xs = range(x2 + 1)

impossible_xs = []
impossible_ys = []

winners = []

for x in possible_xs:
    for y in possible_ys:
        done = False

        x_pos = 0
        y_pos = 0

        x_vel = x
        y_vel = y
        # step

        while not done:
            if x in impossible_xs:
                break

            if x_vel == 0 and x_pos < x1:
                impossible_xs.append(x)
                break

            x_pos += x_vel
            y_pos += y_vel

            x_vel = x_vel - 1 if x_vel > 0 else 0
            y_vel -= 1

            if x1 <= x_pos <= x2 and y2 <= y_pos <= y1:
                winners.append((x,y))
                break

            if x_vel > x2 or y_vel < y2:
                break

        #if y > 0:
            #print((x,y), (x,y) in winners)

print()
print(len(winners))
