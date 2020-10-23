"""
sum-of-terms definition (§2.1)
in base-2, basically just popcount
TLDR: it works and it's correct but it's also slow so dont use it
"""
import itertools


def popcount64(number):
    assert 0 <= number <= 0xFFFFFFFFFFFFFFFF  # max unsigned 64-bit
    number -= ((number >> 1) & 0x5555555555555555)
    number = (number & 0x3333333333333333) + (number >> 2 & 0x3333333333333333)
    return (((number + (number >> 4)) & 0x0F0F0F0F0F0F0F0F) * 0x0101010101010101) & 0xFFFFFFFFFFFFFFFF >> 56


def n_ary(number, n):
    assert n >= 1 and isinstance(n, int)
    if n == 1:
        return [0] * number

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
    assert num_players >= 1 and isinstance(num_players, int)

    # handle singleton case
    if num_players == 1:
        return [0] * min_length

    seq = list(range(num_players))
    i = 0
    while num_players ** i < min_length:
        i += 1
    seqs = list(itertools.product(seq, repeat=i))

    out = [sum(seq) % num_players for seq in seqs]
    return out[:min_length] if trim else out


if __name__ == '__main__':
    n = 343
    min_len = 99999

    print(thue_morse_idx(0, 1))
    print(thue_morse_idx(1, 1))
    print(thue_morse_idx(2, 1))
    print(thue_morse_idx(3, 1))
    #
    #
    # def f1():
    #     return generate(n, min_len)
    #
    #
    # def f2():
    #     return [thue_morse_idx(i, n) for i in range(min_len)]
    #
    #
    # def f3():
    #     return thue_morse_iter(n, min_len)
    #
    #
    # print(len(f1()))
    # print(len(f2()))  # slow
    # print(len(f3()))  # less slow (sometimes)
    #
    # print(list(fair_test(f1, f2, f3, min_len=10, n_iterations=10)))
    # # for 2 players, min_len=99999: (f1 and f3 produce 131072)
    # # [('f1', 2.994079113006592),
    # #  ('f2', 18.689956426620483),  <-- faster than usual because of popcount
    # #  ('f3', 16.79806089401245),
    # # ]
    # # for 7 players, min_len=99999: (f1 and f3 produce 117649)
    # # [('f1', 0.4846773147583008),
    # #  ('f2', 43.50232172012329),
    # #  ('f3', 8.666783809661865),
    # # ]
    # # for 48 players, min_len=99999: (f1 and f3 produce 110592)
    # # [('f1', 0.13373684883117676),
    # #  ('f2', 32.38348436355591),
    # #  ('f3', 7.479870319366455),
    # # ]
    # # for 343 players, min_len=99999: (f1 and f3 produce 117649)
    # # [('f1', 0.5106184482574463),
    # #  ('f2', 23.304750204086304),
    # #  ('f3', 7.471975326538086),
    # # ]
