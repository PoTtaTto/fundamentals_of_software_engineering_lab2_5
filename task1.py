#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    tuple_a = tuple(map(int, input().split()))
    if len(tuple_a) != 10:
        print('Wrong tuple size!', file=sys.stderr)
        exit(1)
    print(sum(item for item in tuple_a if abs(item) < 5))
