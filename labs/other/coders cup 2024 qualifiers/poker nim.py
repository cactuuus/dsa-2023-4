#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pokerNim' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY c
#

def pokerNim(k, c):
    if len(c) == 1:
        return "First"
    c.sort()
    first = (len(c)-2) % 2 != 0
    if (c[0] == 1) != (c[1] == 1): # XOR
        first = not first
    return "First" if first else "Second"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        c = list(map(int, input().rstrip().split()))
        result = pokerNim(k, c)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
