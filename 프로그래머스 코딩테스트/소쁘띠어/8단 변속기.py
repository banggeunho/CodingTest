# https://softeer.ai/practice/info.do?idx=1&eid=408&sw_prbl_sbms_sn=236927
arr = list(map(int, input().split()))

def isAsecending(arr):
    return arr == sorted(arr)

def isDescending(arr):
    return arr == sorted(arr, reverse = True)

if isAsecending(arr):
    print("ascending")

elif isDescending(arr):
    print("descending")

else:
    print("mixed")
