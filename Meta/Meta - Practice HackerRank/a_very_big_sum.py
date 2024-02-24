#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    i = 0
    j = len(ar) - 1
    totalSum = 0
    while i < j:
        totalSum += ar[i]
        totalSum += ar[j]

        i += 1
        j -= 1

    if i == j and len(ar) != 0:
        totalSum += ar[i]

    return totalSum


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + "\n")

    fptr.close()
