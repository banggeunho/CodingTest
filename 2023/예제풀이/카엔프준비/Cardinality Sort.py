import heapq
def sortByBits(arr):
    # Function to calculate number of ones

    def countOnes(n):
        cnt = 0
        while n:
            n = n & (n - 1)
            cnt += 1
        return cnt

    # Calculate number of ones and add them to tmp list as tuple of (number of ones, num)
    tmp = []
    for n in arr:
        ones = countOnes(n)
        heapq.heappush(tmp, (ones, n))

    res = []
    # Extract result
    while tmp:
        res.append(heapq.heappop(tmp)[1])

    return res

print(sortByBits([31, 15, 7, 3, 2]))
print(sortByBits([3]))
print(sortByBits([1,2,3,4,5]))
print(sortByBits([0,1,2,3,4,5,6,7,8]))
print(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))