#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lotto prediction
# Go Namhyeon <gnh1201@gmail.com>
# 2020-12-24

data = {
    '942': [10, 12, 18, 35, 42, 43],
    '941': [12, 14, 25, 27, 39, 40],
    '940': [3, 15, 20, 22, 24, 41],
    '939': [4, 11, 28, 39, 42, 45],
    '938': [4, 8, 10, 16, 31, 36]
}

params = [943, 938] # 예측회차, 시작회차

def mod(seed):
    return 1 + (seed % 45)

def test(a, b):
    score = 0

    intersects = list(set(b) & set(a))
    matched = len(intersects);
    if matched > 2:
        score = 25 * (matched - 2)

    return score

def generate(i, a1, a2, a3):
    nums = []

    for j in range(1, 7):
        num = 0
        while num == 0:
            seed = (i * a1) + (j * a2) + a3
            num = mod(seed)
            if num in nums:
                num = -1
        nums.append(num)

    nums.sort()

    return nums

def simulate(a1=0, a2=0, a3=0, nums=[]):
    score = 0

    if a1 == 0:
        a1 = random.randrange(0, 100000)
    if a2 == 0:
        a2 = random.randrange(0, 100000)
    if a3 == 0:
        a3 = random.randrange(0, 100000)

    for i in range(params[1], params[0]):
        if len(nums) != 6:
            nums = generate(i, a1, a2, a3)
        score += test(nums, data[str(i)])

    return (score, a1, a2, a3)

def main(args):
    score = -1

    for i in range(0, 100000):
        result = simulate()

        _score = result[0]
        a1 = result[1]
        a2 = result[2]
        a3 = result[3]

        if _score > score:
            score = _score
            nums = generate(params[0], a1, a2, a3)
            print("New Record!", "Score:", score, "; P1:", a1, "; P2:", a2, "; P3:", a3, "; Numbers:", nums)

    # $ python3 main.py
    # New Record! Score: 0 ; P1: 27136 ; P2: 10825 ; P3: 48144 ; Numbers: [3, 8, 18, 23, 28, 43]
    # New Record! Score: 25 ; P1: 42519 ; P2: 91055 ; P3: 87388 ; Numbers: [1, 6, 21, 26, 31, 41]
    # New Record! Score: 50 ; P1: 25995 ; P2: 41946 ; P3: 85014 ; Numbers: [1, 7, 13, 19, 25, 31]
    # New Record! Score: 75 ; P1: 77034 ; P2: 31576 ; P3: 28225 ; Numbers: [9, 12, 26, 29, 40, 43]

    return 0;

if __name__ == '__main__':
    import sys
    import math
    import random
    sys.exit(main(sys.argv))
