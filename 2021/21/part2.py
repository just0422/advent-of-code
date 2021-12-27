from collections import defaultdict

possibilities = []
locations = [10] + list(range(1, 10))
p1_score_results = {}
p2_score_results = {}
for x in range(1,4):
    for y in range(1, 4):
        for z in range(1, 4):
            possibilities.append([x,y,z])

def winner(result):
    return (1,0) if result[0] > result[1] else  (0,1)

def roll(p1s, p1l, p2s, p2l, turn, d):
    #print(d*"-", f"{p1s=}, {p2s=} {turn=}")
    if p1s >= 21:
        return 1, 0
    if p2s >= 21:
        return 0, 1


    totals = []
    for scores in possibilities:
        next_score = sum(scores)

        if turn == 1:
            p1_loc = locations[(p1l + next_score) % 10]
            p1_score = p1s + p1_loc
            if (p1_score, p1_loc, next_score) in p1_score_results:
                #print(f"######### {p1s=} {p1l=} {next_score=} -- {p1_score_results[(p1s, p1l, next_score)]}")
                totals.append(p1_score_results[(p1_score, p1_loc, next_score)])
            #if p1_loc >= 10:
            #print(d*"-", turn, p1l, next_score, p1l + next_score, p1_loc, p1s, p1_score)
            # print(f"{p1_score=}")
            result = roll(p1_score, p1_loc, p2s, p2l, 0, d+1)
            #print(d*"-", f"{p1_score=}, {p2s=}, {result=}")
            # print()
            p1_score_results[(p1_score, p1_loc, next_score)] = winner(result)
            totals.append(result)
        else:
            p2_loc = locations[(p2l + next_score) % 10]
            p2_score = p2s + p2_loc
            if (p2_score, p2_loc, next_score) in p2_score_results:
                #print(f"######### {p2s=} {p2l=} {next_score=} -- {p2_score_results[(p2s, p2l, next_score)]}")
                totals.append(p2_score_results[(p2_score, p2_loc, next_score)])
            #if p2_loc >= 10:
            #    print(d*"-", turn, p2l, next_score, p2l + next_score, p2_loc, p2s, p2_score)
            # print(f"{p2_score=}")
            result = roll(p1s, p1l, p2_score, p2_loc, 1, d+1)
            #print(d*"-", f"{p1s=}, {p2_score=}, {result=}")
            # print()
            p2_score_results[(p2_score, p2_loc, next_score)] = winner(result)
            totals.append(result)

    # print(len(p1_score_results), len(p2_score_results))
    p1_scores = sum([x for x, _ in totals])
    p2_scores = sum([y for _, y in totals])
    final_result = (p1_scores, p2_scores)
    # score_results[(p1_scores, p2_scores, turn)] = final_result
    return final_result

print(roll( 0, 4, 0, 8, 1, 0))
