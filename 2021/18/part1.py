import math
from collections import defaultdict

# with open("input.txt") as pairs:

def splisive(number):
    return type(number) == int and number >= 10

def split(number):
    return [math.floor(number / 2), math.ceil(number / 2)]

def explosive(pair, depth):
    if depth >= 4 and type(pair) == list:
        return pair
    return None

def explode(numbers, pair):
    #guaranteed to be numbers
    l_num = pair[0]
    r_num = pair[1]

    if numbers[0] == pair:
        numbers[0] == 0
        numbers[1] += r_num

        return l_num, True # True means left number is returned
    else:
        numbers[1] == 0
        numbers[0] += l_num
        return r_num, False # False means right number is returned

def reduce(numbers, depth):
    if type(numbers[0]) == int and type(numbers[1]) == int:
        return # Not sure what to return yet
    if explosive(numbers[0], depth):
        explode(numbers, numbers[0])
    elif explosive(numbers[1], depth):
        explode(numbers, numbers[1])
    elif splisive(numbers[0]):
        numbers[0] = split(numbers[0])
        return
    elif splisive(numbers[1]):
        numbers[1] = split(numbers[1])
        return
    else:
        reduce(numbers[0], depth + 1)
        reduce(numbers[1], depth + 1)
        return
