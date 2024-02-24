#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def icecreamParlor(m, arr):
    cnt = {}
    for i in range(len(arr)):
        val = m - arr[i]
        if val in cnt:
            return [cnt[val] + 1, i + 1]
        else:
            cnt[arr[i]] = i
    return


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")

    fptr.close()
