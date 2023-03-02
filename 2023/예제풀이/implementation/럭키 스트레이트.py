num = list(map(int, input()))
idx = int(len(num)/2)

if sum(num[:idx]) == sum(num[idx:]):
    print('LUCKY')
else:
    print('READY')
