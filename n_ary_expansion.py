"""
sum-of-terms definition (§2.1)
in base-2, basically just popcount
"""
from collections import Counter

from thue_morse import generate


def n_ary(number, n):
    nums = []
    while number:
        number, r = divmod(number, n)
        nums.append(r)
    return nums[::-1]


def thue_morse_idx(index, dim):
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
