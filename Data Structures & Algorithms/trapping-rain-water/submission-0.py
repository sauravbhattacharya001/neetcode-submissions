class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftmaxindex=0
        waterleft=[0]

        for i in range(1,len(height)):
            if height[i] < height[leftmaxindex]:
                waterleft.append(height[leftmaxindex] - height[i])
            else:
                waterleft.append(0)
                leftmaxindex = i
        
        righmaxindex=len(height)-1
        waterright=deque([0])

        for i in range(len(height)-2,-1,-1):
            if height[i] < height[righmaxindex]:
                waterright.appendleft(height[righmaxindex] - height[i])
            else:
                waterright.appendleft(0)
                righmaxindex = i

        result = []

        for i in range(len(waterleft)):
            result.append(min(waterleft[i], waterright.popleft()))
        
        return sum(result)
        
