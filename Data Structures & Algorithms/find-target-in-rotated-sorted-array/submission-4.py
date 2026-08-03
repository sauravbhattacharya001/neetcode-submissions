class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        lowest = left
        right = len(nums) - 1

        if target > nums[right]:
            right = lowest -1
            left = 0
        else:
            right = len(nums) - 1
            left = lowest

        while left <= right:
            mid = left + (right - left ) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else: 
                return mid
        
        return -1

