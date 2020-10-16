"""
# Interpreter

Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

## Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

["12","insert 0 5","insert 1 10","insert 0 6","print","remove 6","append 9","append 1","sort","print","pop","reverse","print"]

## Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
if __name__ == '__main__':
    result=[]
    execution = dict({
        'insert': lambda r,i,e: r.insert(i,e),
        'print': lambda r: print(r),
        'remove': lambda r,e: r.remove(e),
        'append': lambda r,e: r.append(e),
        'sort': lambda r: r.sort(),
        'pop': lambda r: r.pop(),
        'reverse': lambda r: r.reverse(),
        })
    N = int(input())
    lines = []
    for i in range(N):
        line = input()
        command = line.split(sep=" ")
        params = [int(x) for x in command[1:]]
        execution[command[0]](result,*params)
        
"""
["29","append 1","append 6","append 10","append 8","append 9","append 2","append 12","append 7","append 3","append 5","insert 8 66","insert 1 30","insert 6 75","insert 4 44","insert 9 67","insert 2 44","insert 9 21","insert 8 87","insert 1 75","insert 1 48","print","reverse","print","sort","print","append 2","append 5","remove 2","print"]
"""
"""
[1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
[5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
[1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
[1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]
"""
