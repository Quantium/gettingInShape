from itertools import permutations
posibles,k = input().split()
print(*[''.join(x) for x in permutations(sorted(posibles),int(k))],sep='\n')

"""
You are given a string S.
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

# Input Format
A single line containing the space separated string  and the integer value .

# Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.

# Output Format
Print the permutations of the string  on separate lines.

# Sample Input
HACK 2

# Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.
"""