ZERO =  [1,2,3,4,5,6  ]
ONE =   [  2,3]
TWO =   [1,2,  4,5,  7]
THREE = [1,2,3,4,    7]
FOUR =  [  2,3,    6,7]
FIVE =  [1,  3,4,  6,7]
SIX =   [1,  3,4,5,6,7]
SEVEN = [1,2,3        ]
EIGHT = [1,2,3,4,5,6,7]
NINE =  [1,2,3,4,  6,7]

ONE =   [  2,3]
FOUR =  [  2,3,    6,7]
SEVEN = [1,2,3        ]
TWO =   [1,2,  4,5,  7] # 5
THREE = [1,2,3,4,    7] # 5
FIVE =  [1,  3,4,  6,7] # 5

ONE =   [  2,3]
FOUR =  [  2,3,    6,7]
SEVEN = [1,2,3        ]
ZERO =  [1,2,3,4,5,6  ] # 6
SIX =   [1,  3,4,5,6,7] # 6
NINE =  [1,2,3,4,  6,7] # 6

def compare(characters, digit):
    for c in characters:
        if c not in digit:
            return False
    return True


with open("input.txt") as numbers:
    running_sum = 0
    while (line := numbers.readline().rstrip()):
        io = line.split(' | ')

        inp = io[0].split(' ')
        inp.sort(key=len)

        digit_characters = {}
        for digit in inp:
            if len(digit) == 2:
                digit_characters[1] = digit

            if len(digit) == 3:
                digit_characters[7] = digit

            if len(digit) == 4:
                digit_characters[4] = digit

            if len(digit) == 5:
                four_less_one = digit_characters[4]
                for char in digit_characters[1]:
                    four_less_one = four_less_one.replace(char, "")

                if compare(digit_characters[7], digit):
                    digit_characters[3] = digit
                elif compare(four_less_one, digit):
                    digit_characters[5] = digit
                else:
                    digit_characters[2] = digit

            if len(digit) == 6:
                if compare(digit_characters[4], digit):
                    digit_characters[9] = digit
                elif compare(digit_characters[7], digit):
                    digit_characters[0] = digit
                else:
                    digit_characters[6] = digit

            if len(digit) == 7:
                digit_characters[8] = digit

        character_digits = { ''.join(sorted(v)):k for k,v in digit_characters.items() }

        output = [''.join(sorted(v)) for v in io[1].split(' ')]
        out_value = 0
        for out_digit in output:
            out_value *= 10
            out_value += character_digits[out_digit]

        # F- 1,6,7,[2,3]
        print(out_value)
        running_sum += out_value

    print()
    print(running_sum)
