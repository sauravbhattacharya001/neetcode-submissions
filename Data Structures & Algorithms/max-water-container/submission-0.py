class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0
        right = len(heights) - 1

        maxarea =0

        while left < right:
            height = min(heights[left], heights[right])
            current_height = (right - left) * height
            maxarea = current_height if maxarea < current_height else maxarea

            if height == heights[left]:
                left += 1
            else:
                right -= 1

        return maxarea