import random


def gen_random_initial(input_initial):
    while True:
        rand_initial = chr(random.randint(65, 90))
        if rand_initial not in (input_initial, 'I'):
            return rand_initial

