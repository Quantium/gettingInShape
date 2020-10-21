#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    #Genera una lista seqs de listas vacías. No se usa [[]]*n porque genera una lista con referencias a la misma lista
    seqs=[[] for i in range(n)]
    lastAnswer = 0
    res=[]
    for q in queries:
        #Obtiene la secuencia según la fórmula dada
        seq=seqs[(q[1]^lastAnswer)%n]
        if q[0] == 1:
            #Si es 1 el primer q[0] parametro de la secuencia agrega el tercer q[2] parametro a la secuencia
            seq.append(q[2])
        else:
            # asigna, según la fórmula dada (y%size) donde y es el tercer commando de la secuencia q[2]
            lastAnswer=seq[q[2]%len(seq)]
            res.append(lastAnswer)
    return res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
    print('\n')
