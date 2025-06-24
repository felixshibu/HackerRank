# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
A = set(map(int, input().split(' ')))

for i in range(int(input())):
    command = input().split(' ')
    s = set(map(int, input().split(' ')))

    if command[0] == 'intersection_update':
        A.intersection_update(s)
    elif command[0] == 'update':
        A.update(s)
    elif command[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(s)
    elif command[0] == 'difference_update':
        A.difference_update(s)

print(sum(A))