# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
rooms = list(map(int,input().split(' ')))

rooms_dict = {}

for room in rooms:
    if room not in rooms_dict:
        rooms_dict[room] = 1
    else:
        rooms_dict[room] += 1

for k,v in rooms_dict.items():
    if v == 1:
        print(k)