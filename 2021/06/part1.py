with open("input.txt") as lantern_fish:
    import time
    start_time = time.time()

    fishes = lantern_fish.readline().rstrip()
    fishes = [int(x) for x in fishes.split(',')]

    population = [0] * 9

    for fish in fishes:
        population[fish] += 1

    count = 2**10
    print(count)
    for day in range(count):
        birthing = population.pop(0)

        population[6] += birthing
        population.append(birthing)

    #print(sum(population))
    print("--- %s seconds ---" % (time.time() - start_time))
