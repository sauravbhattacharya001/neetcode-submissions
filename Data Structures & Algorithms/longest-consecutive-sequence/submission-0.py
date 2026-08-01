class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()
        hash = defaultdict(int)
    
        for num in nums:
            myset.add(num)

        for num in myset:
            if num-1 not in myset:
                hash[num] = 1
                curr = num + 1
                while curr in myset:
                    hash[curr] = hash[curr-1] + 1   
                    curr += 1                 

        max = 0
        for item in hash:
            if hash[item] > max:
                max = hash[item]
        return max