turn = 1

p1_score = 0
p2_score = 0

p1_location = 0
p2_location = 9

die = 1
rolls = 0
while p1_score < 1000 and p2_score < 1000:
    next_die_rolls = [die, die + 1, die + 2]
    for x in range(3):
        if next_die_rolls[x] > 100:
            next_die_rolls[x] -= 100

    next_score = sum(next_die_rolls)
    if turn == 1:
        p1_location = (p1_location + next_score) % 10
        p1_score += p1_location + 1
    else:
        p2_location = (p2_location + next_score) % 10
        p2_score += p2_location + 1

    die = (die + 3) % 100
    rolls += 3

    turn = 0 if turn else 1


print(rolls)
print(p1_score)
print(p2_score)
