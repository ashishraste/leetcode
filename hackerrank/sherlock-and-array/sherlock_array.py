import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    size = len(arr)
    if size == 1:
        return 'YES'

    left_totals = [0] * size
    right_totals = [0] * size
    
    left_totals[0] = arr[0]
    for i in range(1, size):
        left_totals[i] = left_totals[i-1] + arr[i]

    right_totals[size-1] = arr[size-1]
    for i in range(size-2, -1, -1):
        right_totals[i] = right_totals[i+1] + arr[i]
    
    for i in range(size):
        if left_totals[i] == right_totals[i]:            
            return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)

        print(result)
    