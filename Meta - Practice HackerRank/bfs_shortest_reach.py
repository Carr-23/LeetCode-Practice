#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


def bfs(n, m, edges, s):
    compl = {s: 0}
    while len(compl) < n:
        edgesCopy = edges[:]

        for edge in edgesCopy:
            if edge[0] in compl or edge[1] in compl:
                if edge[0] not in compl:
                    compl[edge[0]] = 6 + compl[edge[1]]
                elif edge[1] not in compl:
                    compl[edge[1]] = 6 + compl[edge[0]]
                edges.remove(edge)
        if not edges:
            break

    weights = []
    for i in range(1, n + 1):
        if i == s:
            continue
        if i in compl.keys():
            weights.append(compl[i])
        else:
            weights.append(-1)
    return weights


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")

    fptr.close()
