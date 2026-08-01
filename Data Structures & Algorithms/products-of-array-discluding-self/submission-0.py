class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = []
        suffix_mult = deque()
        result=[]
        for index,num in enumerate(nums):
            if (index== 0):
                prefix_mult.append(num)
            else:
                prefix_mult.append(prefix_mult[index-1] * num)

        for index,num in enumerate(nums[::-1]):
            if index == 0:
                suffix_mult.appendleft(num)
            else:
                suffix_mult.appendleft(suffix_mult[0] * num)

        for index, num in enumerate(nums):
            left = 1
            right = 1
            
            if index > 0:
                left = prefix_mult[index-1]            
            if index < len(nums) - 1:
                right = suffix_mult[index+1]

            result.append(left * right)

        return result