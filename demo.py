import numpy as np


def func():
    counts = 0
    numbers = int(input())
    for i in range(numbers):
        if i//2 == 0:
            print("ok")
        else:
            print('not ok')
            counts += 1
    return counts
