#move(n,A,B):
#
#Let C be the third tower (that isn't A or B)
#
#if (n == 1):
#    move the top disk on A to B
#
#if (n>1):
#    move(n-1,A,C)
#    move(1,A,B) # move nth smallest disk from A to B
#    move(n-1,C,B)
#
#|       |       |
#1       |       |
#22      |       |
#333     |       |
#4444    |       |
#55555   |       |
