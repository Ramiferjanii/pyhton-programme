#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    n = len(grid) 
    m= len(grid[0])
    c = 0 
    for i in range(n) :
        for j in range(m) :
            is_d = True 
            for x in range (max(0 , i-1 ) ,  min(n, i+2)) : 
                for y in range (max (0 , j-1) , min (m , j+2))  : 
                    if (x != i or y != j ) and grid [x][y] >= grid[i][j] :
                        is_d = False 
                if not is_d : 
                    break
            if is_d : 
                c += 1 
    
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()