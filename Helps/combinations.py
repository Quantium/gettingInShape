from itertools import combinations
posibles,k = input().split()
print(*[''.join(x) for y in range(1,int(k)+1) for x in combinations(sorted(posibles),int(y))],sep='\n')

"""
You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

# Input Format
A single line containing the string  and integer value  separated by a space.

# Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.

# Output Format
Print the different combinations of string  on separate lines.

# Sample Input
HACK 2

# Sample Output
A
C
H
K
AC
AH
AK
CH
CK
HK
"""