# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for num in range(int(input())):

    print(bool(re.search(r'^[-+]?\d*\.\d+$',input())))
