"""
sum-of-terms definition (§2.1)
in base-2, basically just popcount
"""
from collections import Counter

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


if __name__ == '__main__':

    tm = []
    c = Counter()
    for i in range(1235):
        tmi = thue_morse_idx(i, 5)
        tm.append(tmi)
        c[tmi] += 1

    print(c)
    print(tm[:1000])

    tm2 = generate(5, 1000, trim=True)
    print(tm2)
    print(tm[:1000] == tm2)
