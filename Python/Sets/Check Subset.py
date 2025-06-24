# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
A = set()
B = set()
for i in range(T):
    j = int(input())
    A = set(map(int, input().split(' ')))
    k = int(input())
    B = set(map(int, input().split(' ')))

    if A.issubset(B):
        print(True)
    else:
        print(False)