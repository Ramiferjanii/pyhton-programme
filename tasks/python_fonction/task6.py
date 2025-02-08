#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    b  = 0 
    for i in a : 
        b ^= i  # Great question! The expression unique ^= num is a shorthand for unique = unique ^ num, where ^ represents the XOR (exclusive OR) bitwise operation.
    return b  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
     
    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

    """Given an array of integers, where all elements but one occur twice, find the unique element."""