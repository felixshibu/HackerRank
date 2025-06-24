# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int,input().split(' ')))
n = int(input())
sublist = []
for i in range(n):
    sublist.append(set(map(int,input().split(' '))))

is_superset = True
for subs in sublist:
    if not A.issuperset(subs):
        is_superset = False

print(is_superset)