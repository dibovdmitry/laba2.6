#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys


if __name__ == '__main__':
    Origin = {1: 'a', 2: 'b', 3: 'c'}
    LOL = Origin.items()
    Revers = {v: k for k, v in LOL}
    print(Revers)
