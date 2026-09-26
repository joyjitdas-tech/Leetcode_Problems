class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0
        max_area = 0
        while left < right:
            area = (right-left) * min(height[left],height[right])
            max_area = max(area,max_area)
            print(area)
            
            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return max_area