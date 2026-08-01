class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        countheap = []
        for num, count in counts.items():
            countheap.append((-count, num))

        heapq.heapify(countheap)

        result = []
        while len(result) < k:
            result.append(heapq.heappop(countheap)[1])

        return result