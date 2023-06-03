from collections import Counter
import heapq

def topKFrequent(nums, k):
    a = Counter(nums).most_common(k)
    return [num for num, count in a]

print(topKFrequent([1,1,1,2,2,3], k=2))
######


from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: hash에 frequency 저장
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        print(freq)
        # Step 2: min-heap sort 사용
        heap = []
        for num, count in freq.items():
            if len(heap) < k:  # heap 사이즈가 k보다 작을때
                heapq.heappush(heap, (count, num))

            elif count > heap[0][0]:  # 더 큰 freq가 나타났을때 [0][0]이 항상 작은애가 있음.(min heap이기 때문)
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))

        # # Step 3: Return the elements in the heap
        return [num for count, num in heap]


