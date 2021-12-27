from copy import deepcopy

with open("input.txt") as lights:
    algo = lights.readline().rstrip()
    lights.readline()

    image = []
    while(pixels := lights.readline().rstrip()):
        image.append(list(pixels))

    image_width = len(image[0])
    image_height = len(image)

    for _ in range(image_height):
        image.insert(0, list('.' * image_width))
        image.append(list('.' * image_width))
    for x in range(image_height * 3):
        image[x] = list('.' * image_width) + image[x] + list('.' * image_width)

    image_copy = deepcopy(image)

    for i in range(25):
        for x in range(1, len(image) - 1):
            for y in range(1, len(image[x]) - 1):
                bin_pix = image[x-1][y-1:y+2]
                bin_pix += image[x][y-1:y+2]
                bin_pix += image[x+1][y-1:y+2]

                bin_str = ""
                for char in bin_pix:
                    bin_str += '0' if char == '.' else '1'

                bin_int = int(bin_str, 2)

                image_copy[x][y] = algo[bin_int]

        for x in range(len(image_copy)):
            image_copy[x][0] = '#'
            image_copy[x][len(image_copy[0]) - 1] = '#'
        for y in range(len(image_copy[0])):
            image_copy[0][y] = '#'
            image_copy[len(image_copy) - 1][y] = '#'

        image = deepcopy(image_copy)

        for x in range(1, len(image) - 1):
            for y in range(1, len(image[x]) - 1):
                bin_pix = image[x-1][y-1:y+2]
                bin_pix += image[x][y-1:y+2]
                bin_pix += image[x+1][y-1:y+2]

                bin_str = ""
                for char in bin_pix:
                    bin_str += '0' if char == '.' else '1'

                bin_int = int(bin_str, 2)

                image_copy[x][y] = algo[bin_int]

        for x in range(len(image_copy)):
            image_copy[x][0] = '.'
            image_copy[x][len(image_copy[0]) - 1] = '.'
        for y in range(len(image_copy[0])):
            image_copy[0][y] = '.'
            image_copy[len(image_copy) - 1][y] = '.'

        image = deepcopy(image_copy)

    for x, v in enumerate(image_copy):
        for y, w in enumerate(image_copy[x]):
            print(w, end="")
        print()

    light_count = 0
    for y in image_copy:
        for w in y:
            if w == '#':
                light_count += 1

    print(light_count)
