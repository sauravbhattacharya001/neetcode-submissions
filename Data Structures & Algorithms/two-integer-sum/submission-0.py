class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        for i,n in enumerate(nums):
            if target-n in myHash:
                return [myHash[target-n],i]
            myHash[n]=i
        return []