import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    array = []
    output_str = ''
    for i in range(n):
        array.append(arr[n-i-1])
    print(array)
    for i in range(len(array)):
        output_str += str(array[i]) + ' '
    print((output_str))
