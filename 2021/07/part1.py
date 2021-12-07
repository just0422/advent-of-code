from collections import defaultdict

with open("input.txt") as positions:
    pos_dict = defaultdict(int)

    for pos in positions.readline().rstrip().split(','):
        pos_dict[int(pos)]+=1

    total_distances = []
    for i in range(max(pos_dict.keys()) - min(pos_dict.keys())):
        sub_total_distance = 0
        for k,v in pos_dict.items():
            sub_total_distance += abs(k-i) * v
        total_distances.append(sub_total_distance)

    print(min(total_distances))
