#!/usr/bin/env python
# -- coding: utf-8 --
from time import time
import sys


process = {}

def Hosoya(n, m):
    # Base case
    posi = repr(n) + repr(m)
    if ((n == 0 and m == 0) or
            (n == 1 and m == 0) or
            (n == 1 and m == 1) or
            (n == 2 and m == 1)):
        return 1
    # Memorization check
    if posi in process.keys():
        return process.get(posi)
    # Recursive step
    if n > m:
        # Memorization step
        process[posi] = Hosoya(n - 1, m) + Hosoya(n - 2, m)
        return process.get(posi)
    elif m == n:
        # Memorization step
        process[posi] = Hosoya(n - 1, m - 1) + Hosoya(n - 2, m - 2)
        return process.get(posi)
    else:
        return 0


# Print the Hosoya triangle of height n.
def printHosoya(n,t=0):
    start_time = time()
    for i in range(n):
        for j in range(i + 1):
            if t == 0: print(Hosoya(i, j), end=' ')
            else: Hosoya(i, j)
        if t == 0: print('\n', end="")
    elapsed_time = time() - start_time
    if t == 1: print("Elapse time for ("+repr(n)+"):"+repr(elapsed_time))


def main():
    if len(sys.argv) > 2:
        if sys.argv[1] == "-t":
            for i in range(2,len(sys.argv)):
                printHosoya(int(sys.argv[i]),1)
        else:
            for i in range(2,len(sys.argv)):
                printHosoya(int(sys.argv[i]),0)
    print("Size of map:" , len(process))
main()
