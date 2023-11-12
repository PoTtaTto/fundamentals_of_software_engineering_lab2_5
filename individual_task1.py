#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    tuple_ = tuple(map(int, input('Enter tuple: ').split()))
    if len(tuple_) < 2:
        print('Tuple must contains at least 2 elements!', file=sys.stderr)
    else:
        last_even_pair_index = -1
        for i in range(len(tuple_) - 1, -1, -1):
            if i - 1 != -1:
                cur, prev = i, i - 1
                if tuple_[cur] % 2 == 0 and tuple_[prev] % 2 == 0:
                    last_even_pair_index = prev
                    break
        if last_even_pair_index != -1:
            print([tuple_[i] for i in range(last_even_pair_index)])
        else:
            print('There are no even pairs in tuple!')
