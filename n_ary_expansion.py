"""
sum-of-terms definition (§2.1)
in base-2, basically just popcount
TLDR: it works and it's correct but it's also slow so dont use it
"""
import itertools

from thue_morse import fair_test
from thue_morse import generate


def popcount64(number):
    assert 0 <= number <= 0xFFFFFFFFFFFFFFFF  # max unsigned 64-bit
    number -= ((number >> 1) & 0x5555555555555555)
    number = (number & 0x3333333333333333) + (number >> 2 & 0x3333333333333333)
    return (((number + (number >> 4)) & 0x0F0F0F0F0F0F0F0F) * 0x0101010101010101) & 0xFFFFFFFFFFFFFFFF >> 56


def n_ary(number, n):
    nums = []
    while number:
        number, r = divmod(number, n)
        nums.append(r)
    return nums[::-1]


def thue_morse_idx(index, dim):
    if dim == 2:
        return popcount64(index)
    else:
        return sum(n_ary(index, dim)) % dim


def thue_morse_iter(num_players, min_length, trim=False):
    seq = list(range(num_players))
    seqs = []
    i = 0
    while len(seqs) < min_length:
        i += 1
        seqs = list(itertools.product(seq, repeat=i))

    out = [sum(seq) % num_players for seq in seqs]
    return out[:min_length] if trim else out


if __name__ == '__main__':
    n = 2
    min_len = 99999


    def f1():
        return generate(n, min_len)


    def f2():
        return [thue_morse_idx(i, n) for i in range(min_len)]


    def f3():
        return thue_morse_iter(n, min_len)


    print(len(f1()))
    print(len(f2()))  # slow
    print(len(f3()))  # super slow

    print(list(fair_test(f1, f2, f3, min_len=10, n_iterations=10)))
    # [('f1', 2.8893837928771973),
    #  ('f2', 18.235366582870483),
    #  ('f3', 20.77123260498047),
    # ]
