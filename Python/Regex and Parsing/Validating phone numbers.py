# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    res = re.match(r'^[789]\d{9}$', input())

    print('YES' if res else 'NO')