class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        myset= set()

        for index, i in enumerate(nums):
            if i > len(nums) - 2:
                break            

            left = index + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == -i:
                    
                    if (i, nums[left], nums[right]) in myset:
                        left += 1
                        right -= 1
                        continue

                    myset.add((i, nums[left], nums[right]))                    
                    result.append([i, nums[left], nums[right]])

                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < -i:
                    left += 1
                else:
                    right -= 1

        return result        

"""
DRY RUN
[-1,0,1,2,-1,-4]

[-4,-1,-1, 0,1, 2]

i: -1




"""