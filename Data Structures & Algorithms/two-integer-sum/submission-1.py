class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(int)
        for index, num in enumerate(nums):
            if target-num in hash:
                return [hash[target-num], index]
            hash[num] = index

        return [0,0]