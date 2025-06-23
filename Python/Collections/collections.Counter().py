# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
sizes = list(map(int,input().split(' ')))
N = int(input())

inventory = Counter(sizes)
earned = 0

for i in range(N):
    sale = input().split(' ')
    if inventory[int(sale[0])]:
        inventory[int(sale[0])] -= 1
        earned += int(sale[1])

print(earned)
