"""
fair sequences

morphism definition (§2.4)
basically recursive
"""

import time


def generate(num_players, min_length, trim=False):
    # generate sequences
    seq = list(range(num_players))
    replacement_dict = dict()
    for player_num in range(num_players):
        replacement_dict[player_num] = seq
        seq = seq[1:] + [seq[0]]

    # iterate
    out = [0]
    while len(out) < min_length:
        temp = []
        for item in out:
            temp.extend(replacement_dict[item])
        out = temp

    # return number of rounds divisible by num_players
    return out[:min_length] if trim else out


def fair_test(*functions, min_len=10, n_iterations=100):
    timings = [0] * len(functions)
    for idx in generate(len(functions), len(functions) * min_len):
        timings[idx] -= time.time()
        for _ in range(n_iterations):
            functions[idx]()
        timings[idx] += time.time()
    return [(func.__name__, timing) for func, timing in zip(functions, timings)]


if __name__ == '__main__':

    print(len(generate(3, 100)))
    print(generate(2, 2 ** 2))
    print(generate(2, 4 ** 4))
    print(generate(3, 3 ** 3))
    print(generate(4, 4 ** 4))

    print(''.join('ABCD'[i] for i in generate(4, 50)))

    a = {1: 1}


    def test():
        a = {1: 1}

        def f1():
            nonlocal a
            # for _ in range(10000):
            if 2 in a:
                del a[2]

        def f4():
            global a
            # for _ in range(10000):
            if 2 in a:
                del a[2]

        def f3():
            a = {1: 1}
            # for _ in range(10000):
            if 2 in a:
                del a[2]

        def f2():
            nonlocal a
            # for _ in range(10000):
            try:
                del a[2]
            except KeyError:
                pass

        return fair_test(f1, f4, f3, f2, min_len=1000, n_iterations=10000)


    print(list(test()))
    # [('f1', 1.2600104808807373),
    #  ('f4', 1.3300178050994873),
    #  ('f3', 1.900770664215088),
    #  ('f2', 3.0959300994873047),
    # ]
