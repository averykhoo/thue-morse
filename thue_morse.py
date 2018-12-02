"""
fair sequences
"""

import math
import time


def generate(num_players, min_length, trim=False):
    # need to iterate at least this many times
    iterations = int(math.ceil(math.log(min_length) / math.log(num_players)))
    # need to return this many items
    if trim:
        length = (((min_length + num_players - 1) // num_players) * num_players)
    else:
        length = num_players ** iterations
    # return number of rounds divisible by num_players
    return _generate(num_players, iterations)[:length]


def _generate(num_players, iterations):
    # generate sequences
    seq = list(range(num_players))
    replacement_dict = dict()
    for player_num in range(num_players):
        replacement_dict[player_num] = seq
        seq = seq[1:] + [seq[0]]
    # iterate
    out = [0]
    for _ in range(iterations):
        temp = []
        for item in out:
            temp.extend(replacement_dict[item])
        out = temp
    # return number of rounds divisible by num_players
    return out


def fair_test(*functions, min_len=10):
    timings = [0] * len(functions)
    for idx in generate(len(functions), len(functions) * min_len):
        timings[idx] -= time.time()
        functions[idx]()
        timings[idx] += time.time()
    return [(func.__name__, timing) for func, timing in zip(functions, timings)]


if __name__ == '__main__':


    print(len(generate(3, 100)))
    print(_generate(2, 2))
    print(_generate(2, 4))
    print(_generate(3, 3))
    print(_generate(4, 4))

    print(''.join('asdf'[i] for i in generate(4, 50)))

    def f1():
        a = {1:1}
        for _ in range(100000):
            if 2 in a:
                del a[2]


    def f2():
        a = {1:1}
        for _ in range(100000):
            try:
                del a[2]
            except KeyError:
                pass


    print(list(fair_test(f1, f2, min_len=100)))