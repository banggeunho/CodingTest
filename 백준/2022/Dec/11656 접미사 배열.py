import sys

str = sys.stdin.readline().strip()
prefix = [str]
for i in range(1, len(str)):
    prefix.append(str[i:])

for i in sorted(prefix):
    print(i)
